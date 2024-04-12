import ProfileDetails from "./pages/ProfileDetails";
import SignUp from "./pages/SignUp";
import HomePage from "./pages/HomePage";
import Dashboard from "./pages/Dashboard";

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
		path: "/profileDetails/:category",
		component: ProfileDetails,
		exact: true,
	},
	{
		path: "/dashboard",
		component: Dashboard,
		exact: true,
	}
];
