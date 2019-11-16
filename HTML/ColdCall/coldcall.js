
 let students = [
   'Peter' ,
   'David' ,
   'Harrison',
   'Noah',
   'Sam' ,
   'Gabe',
   'Jack' ,
   'Gus' ,
 ];

// console.log('First element is: ' + students[0]);

// people[1] = 'Rachel';
//
// people.push('Rachel');
//
// people.pop();
// console.log(people);
// console.log('length is' + people.length)
//
// //Getting the index of an element
// console.log(people.indexOf('Josh'))

let everyone = students.concat(students);

let randomIndex =
Math.floor(Math.random()) *
(students.length);

const button =
  document.querySelector('#button');

  const names =
    document.querySelector('#names');

button.addEventListener('click' , (e) => {
  randomNum = Math.floor(Math.random()*students.length);
  console.log(students[randomNum]);
  names.textContent = students[randomNum];
  });
  // nameLabel.innerHTML = students[randNum;
  //   lastNum = randomNumstudents


// console.log('cold call script');
