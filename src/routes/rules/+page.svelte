<script>
	import Hero from '$lib/components/page/Hero.svelte';
	import Content from '$lib/components/page/Content.svelte';
</script>

<svelte:head>
	<title>Rules</title>
</svelte:head>

<Hero>Rules</Hero>

<Content>
	<p>
		The general rules of the competition are described in the <a
			href="https://iio.team/documents/Regulations.pdf"
			class="btn-link link-secondary">IIOT Regulations</a
		>.
	</p>
	<h2 class="text-2xl sm:divider">Technical rules</h2>
	<ul class="list-disc">
		<li>
			Every team will be provided with 2 computers, each with one display, keyboard and mouse. Any
			software on the computer can be used (see the Contest Environment page for more information
			about the available software).
		</li>
		<li>Internet connection will be limited to accessing the grading system only.</li>
		<li>
			Contestants are encouraged to bring their own keyboard (and mouse). However, it must not have
			wireless communication capability and must not have any programmable functions whose
			configuration is retained when unplugged. Own keyboards should be brought to the practice
			session and left in the computer room. Only one keyboard per computer is allowed.
		</li>
		<li>
			In the competition room, blank paper, writing tools, snacks and water will be provided. On the
			competition day, contestants may not bring anything into the competition rooms, except for the
			following items: clothing, ID badge, writing utensils, small mascots, snacks, medicine and
			medical equipment, earplugs and earmuffs.
		</li>
		<li>The only allowed programming language for submitting solutions is C++.</li>
		<li>
			Problem statements will be in English. Each team receives one printed copy of the problem set,
			and all problem statements will be available in the grading system.
		</li>
	</ul>
	<h2 class="text-2xl sm:divider">Online participation rules</h2>
	<ul class="list-disc">
		<li>
			Guest teams may participate online from another venue, however the team must be in one
			location. The rules above should be respected (2 computers per team, limited internet access,
			etc.)
		</li>
		<li>
			The competition venue should be supervised by at least one proctor throughout the contest.
		</li>
		<li>
			All the screens used by the contestants must be recorded with a minimal resolution of 720x1280
			and at least 1 fps during the entire competition.
		</li>
		<li>
			Additionally one or more camera recordings must be made in the contest room such that all the
			team members are visible on the recording. The recording should be saved with a starting
			timestamp (or a clock must be visible on it).
		</li>
		<li>
			The recordings have to be submitted within 3 hours after the competition at a URL provided by
			the organizers.
		</li>
	</ul>
</Content>
