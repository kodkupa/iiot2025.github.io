<script lang="ts">
	import { base } from '$app/paths';
	import MemberCard from '$lib/components/MemberCard.svelte';
	import teams from '$lib/json-data/teams.json';
	import { onMount } from 'svelte';

	let current = 0;
	let flatTeams = teams.regular.concat(teams.guest);

	function next() {
		current = Math.min(current + 1, flatTeams.length - 1);
	}

	function prev() {
		current = Math.max(current - 1, 0);
	}

	function handleKey(e: KeyboardEvent) {
		if (e.key == 'ArrowRight') next();
		else if (e.key == 'ArrowLeft') prev();
	}

	function preloadImages() {
		flatTeams.forEach((team) => {
			team.members.forEach((member) => {
				if (member.picture) {
					const img = new Image();
					img.src = `${base}/images/participants/${member.picture}`;
				}
			});
		});
	}

	onMount(() => {
		preloadImages();
	});
</script>

<svelte:head>
	<title>Teams presentation</title>
</svelte:head>

<svelte:window on:keydown={handleKey} />

<div data-theme="light" class="flex w-full h-full px-8 justify-between items-center">
	<button class="btn btn-circle" on:click={prev} disabled={current === 0}>❮</button>
	<div class="flex flex-col justify-center items-center">
		<h2 class="text-4xl">{flatTeams[current].name}</h2>
		<h3 class="text-xl">{flatTeams[current].country} - {flatTeams[current].school}</h3>
		<div class="flex flex-wrap justify-center gap-6 mt-2">
			{#each flatTeams[current].members as member}
				<MemberCard
					firstName={member.firstName}
					lastName={member.lastName}
					picture={member.picture}
					role={member.role}
				/>
			{/each}
		</div>
	</div>
	<button class="btn btn-circle" on:click={next} disabled={current === flatTeams.length - 1}
		>❯</button
	>
</div>
