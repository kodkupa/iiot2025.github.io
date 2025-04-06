<script>
	import { base } from '$app/paths';
	import Logo from '$lib/components/Logo.svelte';
	import Content from '$lib/components/page/Content.svelte';
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<div
	class="w-full flex justify-center bg-base-200 border-b-[1.5px] border-base-300 shadow-sm z-10 py-6 lg:py-12 px-6"
>
	<div class="max-w-3xl w-full">
		<Logo />
	</div>
</div>

<Content>
	<div class="w-full max-w-4xl text-lg flex flex-col px-2">
		<h2 class="text-2xl sm:divider">IIOT International Final 2025 - Budapest, Hungary</h2>
		<div class="flex flex-col gap-2 text-justify">
			<p>
				The <a href="https://iio.team" class="btn-link link-secondary"
					>International Informatics Olympiad in Teams</a
				>
				(IIOT) is a prestigious computer programming competition for teams of high school students. The
				participants are teams of four high school students representing their schools. The IIOT 2025
				International finals take place in Budapest from May 30 to June 2.
			</p>
			<p>
				The seven regular member countries (Bulgaria, Egypt, Hungary, Italy, Romania, Syria, USA)
				participate with at most 3 teams, and also <b
					>guest teams from any country are invited to take part in the competition onsite or online</b
				>. See the <a href="{base}/registration" class="btn-link link-secondary">registration</a> page
				for more details.
			</p>
		</div>
		<h2 class="text-2xl sm:divider">About IIOT</h2>
		<div class="flex flex-col gap-2 text-justify">
			<p>
				IIOT started in Italy and has been an international competition since 2017. It aims to fill
				an important gap, as there was previously no prestigious programming team competition for
				high school students comparable to the ICPC university competition. However, the problems
				are similar to tasks in the International Olympiad in Informatics (IOI).
			</p>
			<p>
				The competition emphasizes teamwork, creativity, and collaborative learning — skills
				essential in the modern workforce. It includes four online rounds, a national final, and an
				international onsite contest. Each country is coordinated by a leader school or organization
				with support from the international scientific committee. The number of participating
				countries is constantly increasing. To get involved, feel free to reach out to
				<a href="mailto:iio.team@iio.team" class="btn-link link-secondary">iio.team@iio.team</a>.
			</p>
			<p>
				For more information see the IIOT website: <a
					href="https://iio.team/"
					class="btn-link link-secondary">https://iio.team/</a
				>
			</p>
		</div>
	</div>
</Content>

<style>
	h2 {
		font-weight: bold;
		padding-top: 2rem;
		padding-bottom: 1rem;
	}
	h2:first-of-type {
		padding-top: 0 !important;
	}
</style>
