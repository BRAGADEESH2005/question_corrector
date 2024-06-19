import ProfileDetails from "./pages/ProfileDetails";
import SignUp from "./pages/SignUp";
import HomePage from "./pages/HomePage";
import Dashboard from "./pages/Dashboard";
import QuestionPaper from "./pages/QuestionPaper";
import AnswerUpload from "./pages/AnswerUpload";
import ContactUs from "./pages/ContactUs";

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
	},
	{
		path: "/questionPaper",
		component: QuestionPaper,
		exact: true,
	},
	{
		path: "/answerUpload",
		component: AnswerUpload,
		exact: true,
	},
	{
		path:"/contactUs",
		component: ContactUs,
		exact: true,
	}
];
