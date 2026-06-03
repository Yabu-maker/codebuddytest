/**
 * 解析 CSV 文本为二维数组
 * @param {string} text - CSV 原始文本
 * @param {string} sep - 分隔符，默认逗号
 * @returns {string[][]}
 */
function parseCSV(text, sep = ',') {
  const rows = text.trim().split('\n');
  return rows.map(row => {
    const cols = [];
    let cur = '', inQuote = false;
    for (const ch of row) {
      if (ch === '"') { inQuote = !inQuote; continue; }
      if (ch === sep && !inQuote) { cols.push(cur.trim()); cur = ''; continue; }
      cur += ch;
    }
    cols.push(cur.trim());
    return cols;
  });
}

// 示例
const csv = `name,age,city
Alice,28,Beijing
Bob,35,"Shanghai, China"`;
console.table(parseCSV(csv));
