<script>
  import Fa from "svelte-fa/src/fa.svelte";
  import axios from "axios";
  import { faThumbsUp } from "@fortawesome/free-solid-svg-icons";
  import { faPlus } from "@fortawesome/free-solid-svg-icons";
  import { faShare } from "@fortawesome/free-solid-svg-icons";

  export let user_id;
  export let id;

  export let content;

  export let likes;
  export let shares;

  async function getUser(user_id) {
    const path = `http://localhost:5050/users/${user_id}`;

    return await axios.get(path)
                  .then((response) => response.data.user);
  }
</script>

<div class="card">
  <div class="top">
    <div class="profile">
      {#await getUser(user_id)}
        <p>loading</p>
      {:then user}
        <img class="profile-picture" src={user.pfp} alt="profile" />
        <div class="names">
          <span class="nick">
            {user.nick}
          </span>
          <span class="name">
            {"@" + user.name}
          </span>
        </div>
      {/await}
    </div>
  </div>
  <div class="content">
    {content}
  </div>
  <div class="bottom">
    <span class="media-stat like">
      <Fa icon={faThumbsUp} />
      {likes}
    </span>
    <span class="media-stat follow">
      <Fa icon={faPlus} />
    </span>
    <span class="media-stat share">
      <Fa icon={faShare} />
      {shares}
    </span>
  </div>
</div>

<style>
  .card {
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

  .card:hover {
    box-shadow: rgb(199, 185, 185) 0px 0px 15px;
    transition: 0.25s;
  }
  
  .profile {
    display: flex;
    flex-flow: row;
    align-items: center;
    color: white;
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
    text-shadow: darkgray 0px 0px 2px;
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

  .bottom {
    background-color: #1c1c1c;
    padding: 5px;
    height: 40px;
    border-radius: 0px 0px 15px 15px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .media-stat {
    color: white;
    margin: auto;
    font-size: 22px;
  }

  .media-stat:hover {
    cursor: pointer;
    transition: 0.25s;
  }

  .media-stat.like:hover {
    color: rgb(255, 65, 65);
  }

  .media-stat.follow:hover {
    color: gold;
  }

  .media-stat.share:hover {
    color: rgb(0, 155, 255);
  }
</style>
