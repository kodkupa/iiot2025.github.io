<script>
	import { base } from '$app/paths';
	import Content from '$lib/components/page/Content.svelte';
	import Hero from '$lib/components/page/Hero.svelte';
</script>

<svelte:head>
	<title>Registration</title>
</svelte:head>

<Hero>Registration</Hero>
<Content>
	<p class="mx-auto">
		Each team consists of at most 4 students and a team leader. All teams should follow the team
		composition rules (students must be from one school or one region and one institution where they
		learn programming, there can be at most one awarded student per team in the national olympiad in
		programming, see precise details in the <a
			href="https://iio.team/documents/Regulations.pdf"
			class="btn-link link-secondary">IIOT Regulations</a
		> ).
	</p>
	<p>
		Regular member countries can participate with two teams for free (best team of the country and
		best team of the leader school), and an additional team with a 2000 EUR fee that covers all the
		local costs of 4 team members and a team leader (accomodation, food, transportation, etc.). The
		4 committee members (country representative, scientific coordinator, headmaster and teacher of
		the leader school) of each regular member country are also invited.
	</p>
	<p>
		Guest countries can participate onsite with one team for a participation fee of 2000 EUR
		(covering all local costs of 4 team members and a team leader). There is an option for guest
		countries to participate online for free (see <a href="{base}/rules/" class="btn-link link-secondary">
		rules</a> about online participation).
	</p>
	<p>
		The teams and the committee members should be registered using the following two forms.
		<br />
		The <b>deadline for registration is April 30</b>.
	</p>
	<p>
		Team registration form (fill once per team): <a href="https://forms.gle/VxZcQnijx5BdqC5M9" class="btn-link link-secondary">link</a
		>
	</p>
	<p>
		Committee registration form (fill once per country, only regular members): <a href="https://forms.gle/b7WnDJi1RTzv4FrPA" class="btn-link link-secondary"
			>link</a
		>
	</p>
</Content>
