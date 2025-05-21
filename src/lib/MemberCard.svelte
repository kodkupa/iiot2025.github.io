<script lang="ts">
	import { base } from "$app/paths";

	export let firstName: string;
	export let lastName: string;
	export let picture: string;
	export let role: string;

	const monogram = firstName[0] + lastName[0];
</script>

<div class="flex flex-col items-center sm:w-40">
	<figure class="mb-2 rounded-box overflow-hidden shadow-xl w-full aspect-[3/4]">
		{#if picture}
			<img class="w-full h-full object-cover" src="{base}/images/participants/{picture}" alt={firstName + lastName} />
		{:else}
			<span class="flex items-center justify-center w-full h-full bg-base-300 text-5xl font-bold">{monogram}</span>
		{/if}
	</figure>
    <h2 class="font-bold text-center text-lg">{firstName} {lastName}</h2>
    <p class="text-center">{role}</p>
</div>
