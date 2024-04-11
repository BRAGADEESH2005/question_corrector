import ProfileDetails from "./pages/ProfileDetails";
import SignUp from "./pages/SignUp";
import HomePage from "./pages/HomePage";

export const mainRoutes = [
	{
		path: "/",
		component: HomePage,
		exact: true,
	},
	{
		path: "/signup",
		component: SignUp,
		exact: true,
	},
	{
		path: "/profileDetails",
		component: ProfileDetails,
		exact: true,
	},
];
