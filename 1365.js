


var smallerNumbersThanCurrent = function (nums) {
    let count =[]
    let max= Math.max(...nums)
  let each=  nums.map((num) => {
      if (num > max) {
       return count+=1
      }
  })
    return each
};
 console.log(smallerNumbersThanCurrent([8, 1, 2, 2, 3]));


