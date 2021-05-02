// APIService to make requests :/
import APIService from '../index.js';

const ArticleServices = {
	query(){
		// i have=e not create v2 oficialy so it'll be v1 for now
		return APIService.get("articles/api/v1/")
		.catch(err => {
			// now error should get in a ionic alert box
			alert(err);
			throw new Error(err);
		})
		/*
		the query should have some params to like:
		"articles/api/v2/?author=raha?category=web-design"
		*/
	},
	get(slug){
		return APIService.get(`articles/api/v1/${slug}`)
		.catch(err => {
			// now error should get in a ionic alert box
			// trow new Error(err)
			// and som how you should make when ever Error object called it shows in a ionic alert :)
			alert(err);
		})
	}
};

export default ArticleServices;