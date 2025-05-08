<script lang="ts">
	import MemberCard from './MemberCard.svelte';

	export let teams;
</script>

{#each teams as team, i}
	<div>
		<h3 class="text-2xl font-bold w-fit">{team.name}</h3>
		<h4 class="text-lg w-fit">{team.school} - {team.country}</h4>
		<div class="grid grid-cols-2 sm:flex sm:flex-wrap justify-center gap-6 mt-2 w-fit">
			{#each team.members as member}
				<MemberCard firstName={member.firstName} lastName={member.lastName} picture={member.picture} role={member.role} />
			{/each}
		</div>
		{#if i < teams.length - 1}
			<div class="divider" />
		{/if}
	</div>
{/each}
