function handleKeyDown(e) {
  console.log({ e });
}

document
  .getElementById("myBtn")
  .addEventListener("click", function handle(event) {
    console.log({ event });
  });
