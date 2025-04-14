<script>
	import OrgCard from './OrgCard.svelte';
	import Hero from '$lib/components/page/Hero.svelte';
	import Content from '$lib/components/page/Content.svelte';
	import { base } from '$app/paths';
</script>

<svelte:head>
	<title>Organizers & Sponsors</title>
</svelte:head>

<Hero>Organizers & Sponsors</Hero>

<div class="flex flex-wrap justify-center gap-4 px-4 pt-4">
	<OrgCard title="Fazekas" image="fazekas.png">
		The <a href="https://fazekas.hu/" class="btn-link link-secondary">Fazekas Mihály High School</a>
		in Budapest is one of the pillars of talent education in our country. Year after year, its students
		achieve excellent results in the international science olympiads in a wide variety of subjects.
	</OrgCard>
	<OrgCard title="Algo Pro Club" image="algopro.png">
		The <a href="https://algopro.hu/" class="btn-link link-secondary">Algo Pro Club</a> is the first
		competitive programming association in our country. Their online programming courses range from complete
		beginner to international competition level, with a strong emphasis on community building and the
		competitive experience. Several IIOT organisers are members of the association.
	</OrgCard>
	<OrgCard title="NJSZT" image="njszt.png">
		Founded in 1968, the <a href="https://njszt.hu/" class="btn-link link-secondary"
			>Neumann Society</a
		> is a long-established non-profit scientific association. For more than 20 years, its Talent Management
		Department has been involved in organising and preparing for a number of prestigious competitions.
	</OrgCard>
</div>
<Content>
	<h2 class="text-2xl sm:divider">Contact</h2>
	<p class="sm:text-center">
		Main organizer and international coordinator of IIOT: László Nikházy, <a
			href="mailto:iio.team@iio.team"
			class="btn-link link-secondary">iio.team@iio.team</a
		>
	</p>
	<h2 class="text-2xl sm:divider">Sponsors</h2>
	<div
		data-theme="light"
		class="py-4 px-8 bg-base-100 rounded-box flex gap-8 flex-wrap justify-center items-center"
	>
		<img
			class="max-h-36"
			src="{base}/images/logo/eem.png"
			alt="Emberi Erőforrások Minisztériuma logo"
		/>
		<img
			class="max-h-20"
			src="{base}/images/logo/eet.png"
			alt="Emberi Erőforrás Támogatáskezelő logo"
		/>
		<img class="max-h-20" src="{base}/images/logo/ntp.png" alt="Nemzeti Tehetség Program logo" />
	</div>
</Content>
