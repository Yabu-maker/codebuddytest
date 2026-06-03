#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const DB_PATH = path.join(__dirname, '.todos.json');

function loadTodos() {
  try { return JSON.parse(fs.readFileSync(DB_PATH, 'utf8')); }
  catch { return []; }
}

function saveTodos(todos) {
  fs.writeFileSync(DB_PATH, JSON.stringify(todos, null, 2));
}

function add(task) {
  const todos = loadTodos();
  todos.push({ id: Date.now(), task, done: false, createdAt: new Date().toISOString() });
  saveTodos(todos);
  console.log(`✓ 已添加: "${task}"`);
}

function list() {
  const todos = loadTodos();
  if (!todos.length) return console.log('暂无待办事项');
  todos.forEach((t, i) => {
    const status = t.done ? '✅' : '⬜';
    console.log(`${i + 1}. ${status} ${t.task}`);
  });
}

function toggle(id) {
  const todos = loadTodos();
  const todo = todos.find(t => t.id === id);
  if (!todo) return console.log('未找到该事项');
  todo.done = !todo.done;
  saveTodos(todos);
  console.log(`${todo.done ? '✓ 已完成' : '○ 已标记未完成'}: "${todo.task}"`);
}

function remove(id) {
  let todos = loadTodos();
  const before = todos.length;
  todos = todos.filter(t => t.id !== id);
  if (todos.length === before) return console.log('未找到该事项');
  saveTodos(todos);
  console.log(`✗ 已删除`);
}

const cmd = process.argv[2];
const arg = process.argv[3];

switch (cmd) {
  case 'add':    add(arg); break;
  case 'list':   list(); break;
  case 'done':   toggle(Number(arg)); break;
  case 'rm':     remove(Number(arg)); break;
  default:
    console.log(`用法: node todo.js <命令> [参数]
命令:
  add <内容>   添加待办
  list         列出所有待办
  done <id>    切换完成状态
  rm <id>      删除待办`);
}
