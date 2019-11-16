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

let currentlily = 1;

const frog =
  document.querySelector('#frog');


frog.addEventListener('mouseover', (e) => {
  frog.style.height = "80px";
  frog.style.width = "80px";
})
frog.addEventListener('mouseover', (e) => {
  frog.style.height = "70px";
  frog.style.width = "70px";
})

frog.addEventListener('click', (e) => {
  console.log("hop");
  if (currentlily == 1) {
    currentlily= currentlily+1
    frog.style.left = "33.5%";
    frog.style.top = "24%";
    document.querySelector('#lilypad2').classList.add('active')
    document.querySelector('#lilypad1').classList.remove('active')
  }
   else if (currentlily == 2) {
     currentlily= currentlily+1
    frog.style.left = "50%";
    frog.style.top = "50%";
    document.querySelector('#lilypad3').classList.add('active')
    document.querySelector('#lilypad2').classList.remove('active')
  }
  else if (currentlily == 3) {
   currentlily= currentlily+1
   frog.style.left = "68%";
   frog.style.top = "75%";
   document.querySelector('#lilypad4').classList.add('active')
   document.querySelector('#lilypad3').classList.remove('active')
  }
   else if (currentlily == 4) {
    currentlily= currentlily+1
    frog.style.left = "83%";
    frog.style.top = "50%";
    document.querySelector('#lilypad5').classList.add('active')
    document.querySelector('#lilypad4').classList.remove('active')
  }
});

document.addEventListener('keypress' , (e) => {
  if(e.key == " "){
    frog.style.left = "17%";
    frog.style.top = "50%";
    document.querySelector('#lilypad1').classList.add('active');
    document.querySelector('#lilypad5').classList.remove('active');
  }
})
