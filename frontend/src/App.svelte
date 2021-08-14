<script>
  import axios from "axios";
  import Router from "svelte-spa-router";
  import CreateCard from "./components/CreateCard.svelte";
  import Navbar from "./components/Navbar.svelte";
  import Cards from "./routes/Cards.svelte";

  // export let url = "http://localhost:5000";

  let users;
  let cards = [];

  let basepath = "http://localhost:5050";

  function getRoute(route) {
    return `${basepath}/${route}`;
  }
  async function getUser(uid) {
    const path = getRoute(`users/${uid}`);

    return await axios
									.get(path)
									.then(response => response.data.user);
  }

  let uid = "c12073cc-c3c0-468a-9393-f46836b0e607";
</script>

<main>
  {#await getUser(uid)}
    <p>Loading...</p>
  {:then user}
    <Navbar {user} />
  {/await}

  <Router
    routes={{
      "/": Cards,
      "/create": CreateCard,
    }}
  />
</main>

<style>
</style>
