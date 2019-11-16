

let myWakeTime = 9;
let momWakeTime=5;

const myAlarm = (wakeTime) => {
  return("Hey, Sam wake up! It's " + wakeTime);
};
const momAlarm = (momWakeTime) => {
  return("Hey, Mom, wake up! It's" + wakeTime);
};
const familyAlarm = (personCalled, wakeTime) => {
  return 'Hey,' + personCalled + 'wake up'+ "It's" + wakeTime;
};
const importantAlarm = (wakeTime) => {
  return wakeTime.toUpperCase();
};
const snoozeAlarm = (wakeTime) => {
  return 'The alarm for ' + wakeTime + ' has been changed to '+ (wakeTime + 1);
}






// let firstName= 'Samuel'
// const sayHello = () => {
//   let greeting = 'Hello';
//   firstName = 'Jeff';
//   console.log('Hello!' + ' ' + firstName);
// }



// (PRACTICE BELOW)

// setInterval(() => {
//   console.log ('Hello!');
// }, 3000);
