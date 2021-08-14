<script>
	import axios from 'axios';
	import Navbar from './Navbar.svelte'
	import Card from './Card.svelte';
import Fa from 'svelte-fa/src/fa.svelte';

	let users;
	let cards = [];

	let basepath = 'http://localhost:5050'

	function uuidv4() {
		return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    let r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  	});
	}

	function getRoute(route) {
		return `${basepath}/${route}`
	}

	async function getUser(uid) {
		const path = getRoute(`users/${uid}`)

		return await axios
						.get(path)
						.then(reponse => reponse.data.user)
	}

	async function getCards() {
		const path = getRoute('cards')

		return await axios
									.get(path)
									.then(reponse => reponse.data.cards)
	}

	let userID = 'fd96f338-ba68-4f6b-88d9-b272ca61ea33';
</script>

<main>
	{#await getUser(userID)}
		<p>loading...</p>
	{:then user}
  	<Navbar { user } />
	{/await}
  {#await getCards()}
		<p>loading</p>
	{:then cards}
		{#each cards as card}
			<Card {...card} />
		{/each}
	{/await}
</main>

<style>
</style>