import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			fallback: '404.html'
		}),
		paths: {
			base: process.env.NODE_ENV === 'production' ? '/iiot2025.github.io' : ''
		},
		prerender: {
			handleHttpError: 'warn'
		}
	},
	preprocess: vitePreprocess()
};

export default config;
