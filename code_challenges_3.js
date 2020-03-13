function arrayMissing(numArray, maxNum){
    numArray.sort((a, b)=> a - b);
    
    console.log(numArray)
    compareNums = 1
    for(let i = 0; i < maxNum; i++){
        if (numArray[i] == compareNums) {
            compareNums += 1;
        }
        else {
            return compareNums;
        }
    }
}

console.log(
arrayMissing([8,5,2,4,9,7,1,3], 9))
