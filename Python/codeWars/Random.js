function whatIsInAName(collection, source) {
  const arr = [];
  for(let i of collection){
    let c=0;
    console.log(i)
    for(let j of Object.keys(source)){
      if(i[j]==source[j]){
        c+=1;
      }
    }
    console.log(c,Object.keys(source).length)
    if(c==Object.keys(source).length){
      arr.push(i);
    }
    
  }
  return arr;
}
console.log(whatIsInAName([{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }], { "apple": 1 }));