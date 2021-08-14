<script>
  import axios from 'axios';

  export let uid;

  let basepath = 'http://localhost:5050';

  function getRoute(route) {
    return `${basepath}/${route}`
  }

  async function getUser(uid) {
    const path = getRoute(`users/${uid}`);

    return await axios
                  .get(path)
                  .then(response => reponse.data.user);
  }
</script>

{#await getUser(uid)}
  <p>Loading...</p>
  {:then user}
  <div class="create-card">
    <div class="top">
      <div class="profile">
        <img src={user.pfp} alt="Profile" class="profile-picture">
        <div class="names">
          <span class="nick">
            {user.nick}
          </span>
          <span class="name">
            {user.name}
          </span>
        </div>
      </div>
    </div>
    <div class="content">
      <textarea></textarea>
    </div>
  </div>
  <div class="bottom">
    <div class="Post">
      Post
    </div>
  </div>
{/await}

<style>
  .create-card {
    width: 600px;
    height: 340px;
    padding: 5px;
    border-radius: 20px;
    background-color: #3c3c3c;
    color: white;
    margin: auto;
    margin-bottom: 8px;
    box-shadow: black 0px 0px 5px;
  }

  .create-card:hover {
    box-shadow: rgb(200, 185, 185) 0px 0px 15px;
    
    transition: 0.25s;
  }

  .profile {
    display: flex;
    flex-flow: row;
    align-items: center;
    border-radius: 15px 15px 0px 0px;
    background-color: #1c1c1c;
    padding: 5px;
    margin-bottom: 4px;
  }

  .profile-picture {
    width: 60px;
    border-radius: 50%;
  }

  .names {
    display: flex;
    flex-direction: column;
    padding-left: 10px;
  }

  .names span {
    padding: 0;
    margin: -3px;
  }

  .name {
    font-size: 13px;
    padding-bottom: 0;
    color: darkgray;
    text-shadow: darkgray;
  }

  .content {
    font-size: 25px;
    font-weight: bold;
    text-shadow: white 0px 0px 2px;
    padding: 5px;
    background-color: #1c1c1c;
    height: 202px;
    margin-bottom: 4px;
  }
</style>