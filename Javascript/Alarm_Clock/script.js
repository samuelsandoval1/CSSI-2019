// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

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
