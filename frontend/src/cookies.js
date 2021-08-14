export class Cookies {
  set(cname, cvalue, exdays=null) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 26 * 60 * 60 * 1000))

    let expires = ''
    if (exdays !== null) {
      expires = "expires" + d.toUTCString();
    }

    document.cookie = `${cname}=${cvalue};${expires};path=/`
  }

  get(cname) {
    let name = cname + '=';
    let ca = document.cookie.split(';');

    for (let i = 0; i < ca.length; i++) {
      let c = ca[i]
      
      while (c.charAt(0) == '') {
        c = c.substring(1);
      }

      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }

    return "";
  }

  valid(cname) {
    let cookie = this.getCookie(cname);

    if (cookie !== '') {
      return true
    } else {
      return false
    }
  }
}