<script>
	import '../../app.css';
	import '@fortawesome/fontawesome-free/css/all.min.css';

	import Navigation from '$lib/components/Navigation.svelte';

	import { base } from '$app/paths';
	import Up from '$lib/components/Up.svelte';

	let year = new Date().getFullYear();
</script>


<div class="min-h-screen w-full flex flex-col items-center">
	<Navigation />
	<Up />

	<main class="w-full grow flex flex-col items-center bg-base-100 pb-8">
		<slot />
	</main>

	<footer class="footer gap-6 footer-center p-10 bg-base-300 text-base-content">
		<div class="join join-vertical w-full xs:w-fit xs:join-horizontal gap-0">
			<a href="{base}/images/logo-pack.zip" download class="join-item origin-right btn btn-sm xs:btn-md normal-case btn-outline border-neutral">Logo pack</a>
			
			<a class="join-item btn btn-sm xs:btn-md btn-outline border-neutral normal-case" href="mailto:iio.team@iio.team">iio.team@iio.team</a>
			
			<a href="https://www.facebook.com/iio.team/" class="join-item origin-left btn btn-sm xs:btn-md btn-outline border-[#3b5998] bg-[#3b5998] hover:bg-[#273b65] hover:border-[#273b65]">
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" class="fill-white"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path></svg>
			</a>
		</div>
		<div class="flex flex-wrap gap-1">
			<p class="opacity-90">Copyright © {year} - IIOT</p>
			<a href="{base}/documents/privacy_policy.pdf" class="btn-link link-secondary">Privacy Policy</a>
		</div>
	</footer>
</div>
