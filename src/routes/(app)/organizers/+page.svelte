<script>
	import OrgCard from './OrgCard.svelte';
	import Hero from '$lib/components/page/Hero.svelte';
	import Content from '$lib/components/page/Content.svelte';
	import SponsorTile from './SponsorTile.svelte';
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
	<div class="flex flex-wrap justify-center items-center mx-auto gap-4 mt-4 rounded-box">
		<SponsorTile href="https://www.janestreet.com/" logo="janestreet.svg" alt="Jane Street" height={12} />
		<div class="flex gap-4">
			<SponsorTile href="https://atomeromu.mvm.hu/" logo="mvmpaks.png" alt="MVM Paksi Atomerőmű" height={9} />
			<SponsorTile href="https://www.efaktorzrt.hu/" logo="efaktor.png" alt="e-Faktor Zrt" height={9} />
		</div>
		<div class="flex gap-4">
			<SponsorTile href="https://kormany.hu/kulturalis-es-innovacios-miniszterium" logo="KIM.png" alt="Kulturális és Innovációs Minisztérium" height={5} />
			<SponsorTile href="https://nemzetitehetsegprogram.hu/" logo="ntp.png" alt="Nemzeti Tehetség Program" height={5} />
		</div>
	</div>
</Content>
