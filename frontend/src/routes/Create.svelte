<script>
  import CreateCard from "../components/CreateCard.svelte";

  export let uid; // user id
</script>

<div class="create">
  <CreateCard {uid} />
</div>

<style>

</style>