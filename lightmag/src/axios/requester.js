import axios from 'axios';

/* api server address */

/* local */
const base_URL = "http://127.0.0.1:8000/";

/* orginal */
// const base_URL = 'https://ubuntuarchpaperfriendspals-lightmag.ir/';

const requester = axios.create({
	baseURL: base_URL
})

export default requester