<script>
  import axios from 'axios';
  import Card from '../components/Card.svelte';

  let basepath = 'http://localhost:5050'

  function getRoute(route) {
    return `${basepath}/${route}`
  }

  async function getCards() {
    const path = getRoute('cards');

    return await axios
                  .get(path)
                  .then(res => res.data.cards)
  }
</script>

<div class="cards">
  {#await getCards()}
    <p>Loading...</p>
  {:then cards}
    {#each cards as card (card.id)}
      <Card {...card}/>
    {/each}
  {/await}
</div>

<style>

</style>