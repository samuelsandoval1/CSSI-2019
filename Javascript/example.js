let firstName = 'Samuel';
let lastName = 'Sandoval';
let age = 27;


// Function for determining if you can drive.
const canYouDrive = (personAge) => {
if (age >= 18) {
   return 'You can get a license!';
 } else if (age >= 16) {
  return 'You can get a permit!'
 } else if (age >= 8){
  return 'Do not drive!!!!!!';
 } else {
  return 'What are you doing on this site';
 }
 console.log('I am here!')
};
