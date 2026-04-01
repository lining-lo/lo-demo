#!/usr/bin/env node

const { Command } = require("commander");
const inquirer = require("inquirer");
const chalk = require("chalk");
const ora = require("ora");
const fs = require("fs-extra");
const path = require("path");
const spawn = require("cross-spawn");

const program = new Command();

program
  .name("my-cli")
  .version("1.0.0")
  .description("我的极简前端脚手架（本地模板版）");

program
  .command("create <projectName>")
  .description("创建一个新的前端项目")
  .action(async (projectName) => {
    // 1. 选择模板
    const { template } = await inquirer.prompt([
      {
        type: "list",
        name: "template",
        message: "请选择项目模板：",
        choices: [{ name: "Vue3 基础模板", value: "vue-basic" }],
      },
    ]);

    // 2. 路径定义
    const templatePath = path.resolve(__dirname, "../templates", template);
    const projectPath = path.resolve(process.cwd(), projectName);

    // 3. 判断目录是否已存在
    if (fs.existsSync(projectPath)) {
      console.log(chalk.red("❌ 项目已存在！"));
      return;
    }

    // 4. 复制本地模板（无网络、零报错）
    const spinner = ora("🚀 正在生成项目...").start();
    try {
      await fs.copy(templatePath, projectPath);
      spinner.succeed("✅ 项目创建成功！");

      // 5. 修改 package.json 项目名
      const pkg = await fs.readJson(projectPath + "/package.json");
      pkg.name = projectName;
      await fs.writeJson(projectPath + "/package.json", pkg, { spaces: 2 });

      // 6. 是否安装依赖
      const { install } = await inquirer.prompt([
        {
          type: "confirm",
          name: "install",
          message: "是否自动安装依赖？",
          default: true,
        },
      ]);

      if (install) {
        const installSpinner = ora("📦 正在安装依赖...").start();
        spawn("npm", ["install"], { cwd: projectPath, stdio: "inherit" }).on(
          "close",
          () => {
            installSpinner.succeed("✅ 依赖安装完成！");
            console.log(
              chalk.blue(`👉 启动：cd ${projectName} && npm run dev`),
            );
          },
        );
      }
    } catch (err) {
      spinner.fail("❌ 项目生成失败：" + err.message);
    }
  });

program.parse(process.argv);
