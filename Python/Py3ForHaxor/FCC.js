function rangeOfNumbers(startNum, endNum) {
    if(endNum+1==startNum){return [];}
    else{
      const arr=rangeOfNumbers(startNum, endNum-1);
      arr.push(endNum);
      return arr;
    }
  };

var a=rangeOfNumbers(5,10);
console.log(a[])
