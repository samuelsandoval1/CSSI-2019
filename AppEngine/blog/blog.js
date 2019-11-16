const headerElement =
  document.querySelector('#header');

setTimeout(() => {
  headerElement.style.color = 'lime';
} , 3000);

//  ^^^Controls the title header ^^ //




const subheaderElement =
  document.querySelector('#subheader span');

  subheaderElement.addEventListener('mouseover',() => {
    subheaderElement.style.color = 'blue';
  });
  subheaderElement.addEventListener('mouseleave',() => {
    subheaderElement.style.color = '#73a9ff';
  });




  // subheaderElement.addEventListener('mouseover',() => {
  //   subheaderElement.style.color = 'blue';
  // )};
  //
  // subheaderElement.addEventListener('click',() => {
  //   subheaderElement.style.color = 'red';
  // )};




  //  ^^^Controls the subheader ^^ //
