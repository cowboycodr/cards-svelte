<script>
  import axios from "axios";

  export let user;

  document.addEventListener("scroll", handleNavbarScroll);

  function handleNavbarScroll(e) {
    let navbar = document.getElementById("navbar");
    let profileContainer = document.getElementById("profile-container");

    let effectedByScroll = [
      'navbar',
      'profile-container',
      'create-button',
    ]

    if (window.scrollY >= navbar.offsetHeight) {
      effectedByScroll.forEach(function(item, index) {
        let element = document.getElementById(item);

        element.classList.add('scrolled')
      })
    } else {
      effectedByScroll.forEach(function(item, index) {
        let element = document.getElementById(item);

        element.classList.remove('scrolled')
      })
    }
  }

  let basepath = "http://localhost:5050";

  function getRoute(route) {
    return `${basepath}/${route}`;
  }

  console.log(user.id);
</script>

<div class="navbar scrolled" id="navbar" use:handleNavbarScroll>
  <img
    class="profile-picture"
    src={user.pfp}
    alt="profile"
    style="width:60px;height:60px;"
  />
  <div class="profile-container scrolled" id="profile-container">
    <div class="nick">
      {user.nick}
    </div>
    <div class="name">
      {"@" + user.name}
    </div>
  </div>
  <div class="create-button-container">
    <button class="create-button scrolled" id="create-button">
      Create
    </button>
  </div>
</div>

<style>
  .navbar {
    width: 100%;
    height: 75px;
    background-color: black;
    display: flex;
    margin-bottom: 8px;
  }

  .navbar.scrolled {
    position: sticky;
    top: 0px;
    z-index: 9999;
    display: flex;
    top: 8px;
    width: 99%;
    height: 75px;
    margin: auto;
    margin-bottom: 5px;
    background-color: rgba(32, 32, 32, 0.6);
    backdrop-filter: blur(8px) !important;
    border-radius: 20px;
    margin-bottom: 8px;
    box-shadow: black 0px 0px 10px !important;

    transition: 0.25s;
  }

  .profile-picture {
    border-radius: 50%;
    align-self: center;
    margin-left: 8px;
  }

  .profile-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-left: 8px;
  }

  .profile-container.scrolled {
    background-color: #3e3e3e;
    border-radius: 5px;
    transition: 0.25s;
  }

  .nick {
    color: white;
    font-size: 18px;
    /* background-color: #3e3e3e; */
    border-radius: 5px;
  }

  .name {
    color: white;
    font-size: 13px;
    color: rgb(115, 115, 115);
  }

  .create-button-container {
    margin-left: auto;
    width: 10%;
    min-width: 75px;
    max-width: 135px;
    /* align-self: center; */
  }

  .create-button {
    align-self: center;
    height: 100%;
    width: 100%;
    border-radius: 0;
    font-size: 20px;
    text-shadow: black 0px 0px 2px;
  }

  .create-button.scrolled {
    border-radius: 0px 20px 20px 0px;
    box-shadow: white 0px 0px 15px
  }

  .create-button:hover {
    background-color: black;
    color: white;
    box-shadow: black 0px 0px 15px;
    border: 1px solid black;

    transition: 0.25s;
  }

</style>
