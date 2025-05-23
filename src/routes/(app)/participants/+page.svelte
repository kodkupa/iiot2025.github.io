<script lang="ts">
	import { base } from '$app/paths';
	import Hero from '$lib/components/page/Hero.svelte';
	import { regular, guest } from '$lib/json-data/teams.json';
	import MemberList from '$lib/components/MemberList.svelte';
</script>

<svelte:head>
	<title>Participants</title>
</svelte:head>

<Hero>Participants</Hero>

<a href="{base}/participants/presentation" class="btn mt-8 btn-primary" >Go to presentation</a>

<div class="flex flex-col items-center py-8 px-4">
	<h2 class="text-2xl divider mb-8">Regular Teams</h2>
	<MemberList teams={regular} />
	<h2 class="text-2xl divider !mt-16">Guest Teams</h2>
	<MemberList teams={guest} />
</div>
