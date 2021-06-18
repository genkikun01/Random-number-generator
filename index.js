    console.log(Math.random())
//And
let len = 8;
let str = "abcdefghijklmnopqrstuvwxyz";
let strLen = str.length;
let result = "";
 
for (let i = 0; i < len; i++) {
  result += str[Math.floor(Math.random() * strLen)];
}
 
console.log(result);
