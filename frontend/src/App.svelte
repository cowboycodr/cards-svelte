<script>
	import axios from 'axios';
	import { Router, Route, Link } from "svelte-navigator";
	import Navbar from './components/Navbar.svelte'
	import Cards from './routes/Cards.svelte';

	// export let url = "http://localhost:5000";

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

	let userID = 'fd96f338-ba68-4f6b-88d9-b272ca61ea33';
</script>

<Router>
	<header>
		<Navbar uid={userID} />
	</header>

	<Route path="/">
		<Cards />
	</Route>
</Router>

<style>
</style>