document.addEventListener("DOMContentLoaded", function () {
  
  document.querySelectorAll(".likeBtn").forEach((btn) => {
    btn.addEventListener("click", function () {
      const projectID = btn.dataset.post;
      const likeCount = document.querySelector(
        `.likeCount[data-post="${projectID}"]`
      );

      fetch(`like/${projectID}`, {
        method: "PUT",
        body: JSON.stringify({
          likes: likeCount,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          likeCount.innerHTML = data.likes;
        });
    });
  });
});
