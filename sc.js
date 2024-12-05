// Fetch data from a public API and display it in the console
async function fetchData() {
  const apiUrl = "https://jsonplaceholder.typicode.com/posts";

  try {
    // Fetching data from the API
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // Log the fetched data
    console.log("Fetched Data:", data);

    // Process the data: Extracting titles of the first 5 posts
    const topPosts = data.slice(0, 5).map(post => ({
      id: post.id,
      title: post.title,
    }));

    console.log("Top 5 Posts:");
    topPosts.forEach(post => console.log(`ID: ${post.id}, Title: ${post.title}`));
  } catch (error) {
    console.error("Error fetching data:", error.message);
  }
}

// Call the function
fetchData();
