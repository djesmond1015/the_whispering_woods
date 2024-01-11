from enum import Enum

START_SCENE = "Enter woods"
END_SCENE = "Escape woods"

# properties of text dict: narratives, dialogues, choices
# create a constant variable for text dict


class SceneText(Enum):
    NARRATIVES = "narratives"
    DIALOGUES = "dialogues"
    CHOICES = "choices"


# scenes = [
#     {
#         "name": "Find distress flare",
#         "text": {
#             SceneText.NARRATIVES: [
#                 "Amidst the relics of the old cabin, your eyes catch a glint in a dark corner. As you investigate further, you uncover a forgotten storage compartment. Within it lies a distress flare, its red casing standing out in stark contrast to the muted tones of the cabin. The distress flare, nestled among forgotten possessions, seems like a relic from a time when this cabin served as a refuge. Its vibrant red casing suggests a tool meant for urgent communication, evoking questions about the events that unfolded within the subterranean depths."
#             ]
#         },
#         "choice": {},
#         "continue": (True, "Meet rescue team"),
#     },
#     {
#         "name": "Meet rescue team",
#         "text": {
#             SceneText.NARRATIVES: [
#                 "With the distress flare in hand, you decide to utilize its potential, recognizing it as a tool that can bridge the gap between the subterranean depths and the surface world. As you ignite the flare, its vivid red glow fills the chamber, casting an eerie yet captivating light on the old cabin's timeworn interior. The glow of the flare becomes a beacon that cuts through the darkness, signalling not only your presence but also the urgency of your situation. As the radiant glow of the distress flare permeates the hidden chamber, a distant rumble accompanied by voices that grow louder with each passing moment. The voices draw nearer, and the language spoken is one of familiarity—a rescue team, their words laced with concern and purpose.",
#                 "As the rescue team's footsteps draw near, a subtle shift in the atmosphere envelops the hidden cave. The woods beyond the cave seems to sigh, the once vibrant glow of crystals dims, and the eerie luminescence that danced upon timeworn walls begins to fade. It's as if everything in this whispering woods, aware of the approaching presence, desires to keep its secrets concealed. As the rescue team's flashlights pierce the darkness, the once enchanted woods now appears like any forgotten relic of the past. The rescue team leads you through the woods, the trees giving way to moonlit paths.",
#             ]
#         },
#         "choice": {},
#         "continue": (True, END_SCENE),
#     },
#     {
#         "name": END_SCENE,
#         "text": {
#             SceneText.NARRATIVES: [
#                 "The journey, once fraught with mystery and danger, now transforms into a triumphant escape. As you step into the clearing, in a gesture of acknowledgment, the ancient trees in the woods seem to bow as you step beyond the woods' edge, emerging from the thrilling adventure into the embrace of the night, leaving the mysteries of the whispering woods behind. The woods, though left behind, becomes a part of a tale you will tell in the future—a forbidden adventure that unfolded amidst the shadows and secrets of a realm touched by magic, that will forever a lingering sense of wonder in your heart. As you step into the night, guided by the moon and the echoes of an unforgettable journey, the whispering woods continue to whisper its ancient secrets, awaiting for the next adventurer."
#             ]
#         },
#         "choice": {},
#         "continue": (False, None),
#     },
# ]

scenes = [
    {
        "name": START_SCENE,
        "text": {
            SceneText.NARRATIVES: [
                "You stand at the edge of the forbidden woods, a place shrouded in mystery and whispered tales. The air is thick with an unsettling stillness as the ancient trees loom overhead, their gnarled branches creating an intricate canopy that blocks out most of the sunlight. The locals have always avoided this place, speaking in hushed tones of eerie singing echoing through the trees at night and strange conversations that seem to linger in the air.",
                "Despite the warnings, an unexplainable force draws you in. The allure of the unknown pulls at your curiosity, urging you to step beyond the boundary that separates the ordinary from the extraordinary. As you take your first step into the shadowy embrace of the forbidden woods, the outside world fades away, and the air becomes charged with a palpable energy.",
                "The crunch of fallen leaves beneath your feet is the only sound breaking the silence. The path ahead is unclear, and every tree seems to hold its secrets. You can feel the weight of the unseen eyes watching, and the air seems to whisper with the echoes of those who ventured here before. The choices you make now will shape your destiny in this mysterious realm.",
            ]
        },
        "choice": {},
        "continue": (True, "Enter woods 2"),
    },
    {
        "name": "Enter woods 2",
        "text": {
            SceneText.NARRATIVES: [
                "As you delve deeper into the whispering woods, the echoes of mysterious whispers grow more pronounced, swirling around you like a haunting melody. Simultaneously, the surroundings come alive with the soft glow of glimmering fireflies. They dance in erratic patterns, leading you towards different paths, each flicker an invitation to the unknown.",
            ],
            SceneText.DIALOGUES: [
                'Whispers of the Unknown: "The ethereal whispers seem to beckon from the shadows, enticing you with promises of secrets untold. Come closer, seeker, and unravel the mysteries that lie hidden in the heart of the woods."',
                'Glimmering Fireflies: "The fireflies twinkle with an otherworldly allure, guiding you along a path illuminated by their gentle glow. Each step seems to deepen the connection between you and the mystical energy that pulses through the woods."',
                'The Hill\'s Call: "The silhouette of a hill emerges in the distance, its peak shrouded in mist. A faint but distinct pull urges you to ascend, as if the hill itself holds a key to understanding the secrets that linger in the air."',
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Follow the Whispers",
                "[2] - Chase the Fireflies",
                "[3] - Climb the Hill",
            ],
        },
        "choice": {
            "1": "Follow whispers",
            "2": "Chase fireflies 1",
            "3": "Climb hill",
        },
        "continue": (False, None),
    },
    {
        "name": "Follow whispers",
        "text": {
            SceneText.NARRATIVES: [
                "Entranced by the mysterious whispers, you choose to follow their elusive call. The woods seems to respond to your decision, guiding you through a labyrinth of twisted trees and concealed pathways. The ethereal voices lead you to the heart of an ancient grove, where a weathered marker stands, covered in cryptic symbols.",
            ],
        },
        "choice": {},
        "continue": (True, "Discover ancient marker"),
    },
    {
        "name": "Discover ancient marker",
        "text": {
            SceneText.NARRATIVES: [
                "The marker, adorned with symbols of a forgotten language, exudes an energy that resonates with the very essence of the woods. As you decipher the symbols, a hidden passage through the dense foliage is revealed. Intrigued, you push through the bushes, each step echoing with the subtle protests of the entangled vegetation.",
            ],
            SceneText.DIALOGUES: [
                "Ancient Marker's Echo: \"The ancient marker's symbols echo in your mind, carrying a message that transcends language. It hints at a connection between the past and the present, as if the forest itself is a living tapestry woven with threads of time.\"",
                'Unseen Whispers: "The rustling leaves seem to murmur in a language you can\'t quite grasp. The unseen whispers echo through the overgrown trail, guiding you with an uncanny familiarity."',
            ],
        },
        "choice": {},
        "continue": (True, "Traverse though bushes"),
    },
    {
        "name": "Traverse though bushes",
        "text": {
            SceneText.NARRATIVES: [
                "Emerging on the other side, the woods transforms. The air is thick with an ancient magic, and the surroundings are bathed in a soft, golden light filtering through the dense canopy.",
            ],
            SceneText.DIALOGUES: [
                'Rustling of Destiny: "The rustling in the nearby foliage is a constant companion, a symphony of anticipation as you stand at the threshold of the overgrown trail. The air seems to vibrate with the energy of unseen forces, urging you to explore the mysteries that await."',
            ],
        },
        "choice": {},
        "continue": (True, "Hear rustling in nearby foliage"),
    },
    {
        "name": "Chase fireflies 1",
        "text": {
            SceneText.NARRATIVES: [
                "As you choose to follow the captivating dance of the glimmering fireflies, their radiant glow leads you deeper into the heart of the whispering woods. The surroundings become increasingly enchanted, with vibrant flora and bio-luminescent moss creating an otherworldly ambiance. The air is thick with an ancient magic that seems to respond to the presence of the flickering fireflies.",
            ],
        },
        "choice": {},
        "continue": (True, "Chase fireflies 2"),
    },
    {
        "name": "Chase fireflies 2",
        "text": {
            SceneText.NARRATIVES: [
                "Gradually, the glow intensifies, casting an ethereal light that guides you through a dense thicket. The path becomes narrower, and the forest canopy closes overhead, enveloping you in a dim twilight. You descend into a realm where shadows play tricks on the eyes, and the only constant is the mesmerizing dance of the fireflies.",
                "Suddenly, the radiant glow vanishes, plunging you into complete darkness. A hushed silence surrounds you, broken only by the distant sounds of rustling foliage. As your eyes adjust to the absence of light, you discern a faint luminescence ahead.",
            ],
            SceneText.DIALOGUES: [
                'Unseen Whispers: "The rustling leaves seem to murmur in a language you can\'t quite grasp. The unseen whispers echo through the overgrown trail, guiding you with an uncanny familiarity."',
            ],
        },
        "choice": {},
        "continue": (True, "Descend into darkness"),
    },
    {
        "name": "Descend into darkness",
        "text": {
            SceneText.NARRATIVES: [
                "Emerging from the darkness, the foliage appears to part reluctantly, revealing a forgotten path obscured by years of neglect. The air is charged with an eerie stillness, and the rustling sounds persist, beckoning you to explore the hidden secrets that lie ahead.",
            ],
            SceneText.DIALOGUES: [
                'Rustling of Destiny: "The rustling in the nearby foliage is a constant companion, a symphony of anticipation as you stand at the threshold of the overgrown trail. The air seems to vibrate with the energy of unseen forces, urging you to explore the mysteries that await."',
            ],
        },
        "choice": {},
        "continue": (True, "Hear rustling in nearby foliage"),
    },
    {
        "name": "Hear rustling in nearby foliage",
        "text": {
            SceneText.NARRATIVES: [
                "The path ahead reveals itself as an overgrown trail, as if time itself has sought to conceal the secrets that lie within. The overgrown trail bears the marks of an ancient passage, a forgotten artery of the forest. As you step further, the air becomes dense with the weight of time, and the surroundings echo with the lingering essence of something long dormant.",
            ],
            SceneText.DIALOGUES: [
                'Whispers of Recognition: The whispers around you seem to resonate with approval, as if the woods acknowledges your choice. "You tread a path long forgotten, seeker. What awaits you is intertwined with the very roots of this sacred realm."',
            ],
        },
        "choice": {},
        "continue": (True, "Discover an overgrown trail"),
    },
    {
        "name": "Discover an overgrown trail",
        "text": {
            SceneText.NARRATIVES: [
                "As you traverse the overgrown trail, your keen eyes catch a glimpse of something half-buried beneath a carpet of fallen leaves and moss. Kneeling down, you uncover an old, weathered map, its edges frayed with age. The map unfolds, revealing intricate details of the whispering woods, marked with symbols that hint at hidden wonders and potential perils."
            ],
            SceneText.DIALOGUES: [
                'Whispers of the Map: "The map seems to resonate with the ancient energies of the forest. Faint whispers emanate from the parchment, inviting you to decipher the symbols that hold the key to the labyrinthine secrets that surround you."',
            ],
        },
        "choice": {},
        "continue": (True, "Uncover old map"),
    },
    {
        "name": "Uncover old map",
        "text": {
            SceneText.NARRATIVES: [
                "As you carefully examine the ancient map, the forest around you seems to hush into a profound stillness. It's then that you catch a distant, haunting melody, carried on a gentle breeze that rustles through the leaves. The notes are elusive, yet enchanting, weaving through the air like the threads of an ethereal tapestry.",
                "The melody resonates with a timeless grace, beckoning you to follow its trail. The forest, once silent, now comes alive with the enchanting strains, as if the very trees are humming in harmony. The old map in your hands seems to vibrate with an energy that mirrors the melody, as if the two are entwined in an ancient dance.",
            ],
            SceneText.DIALOGUES: [
                'Echoes of the Melody: The forest whispers, and the echoes of the distant melody seem to carry a message of secrets and revelations. "Follow the song, seeker, and you may find answers to questions yet unasked."',
                "Enchanted Harmonies: The melody weaves through the air with an enchanting allure, transcending the boundaries of time. It speaks a language that the heart understands, and its call tugs at the strings of your very soul.",
            ],
        },
        "choice": {},
        "continue": (True, "Hear a distant melody"),
    },
    {
        "name": "Hear a distant melody",
        "text": {
            SceneText.NARRATIVES: [
                "As you stand at this crossroads—map in hand and the distant melody echoing through the ancient trees—the forest holds its breath, awaiting your decision. The choices made now will ripple through the tapestry of the forbidden realm, shaping the narrative that unfolds with each step. What will be your next move in this mysterious journey?"
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Study the Map",
                "[2] - Follow the Melody",
            ],
        },
        "choice": {
            "1": "Study the map",
            "2": "Follow the melody",
        },
        "continue": (False, None),
    },
    {
        "name": "Climb hill",
        "text": {
            SceneText.NARRATIVES: [
                "Ignoring the seductive calls of the echoing whispers and the enchanting allure of the glimmering fireflies, you trust your instincts and ascend the hill looming before you. The climb is steep, and each step feels like a deliberate challenge set by the ancient landscape. As you reach the summit, the forest below unfolds like a mysterious tapestry."
            ]
        },
        "choice": {},
        "continue": (True, "Discover hidden altar"),
    },
    {
        "name": "Discover hidden altar",
        "text": {
            SceneText.NARRATIVES: [
                "You notice a secluded clearing, and at its center stands a weathered stone altar, bathed in the soft glow of the dappled sunlight. The altar bears intricate carvings, hinting at a forgotten purpose. It seems to resonate with the heartbeat of the woods. Faint echoes of ancient rituals linger in the air, inviting you to unravel the mysteries concealed within the carvings. The air is charged with a subtle energy, as if the hill itself is a guardian of ancient secrets."
            ],
            SceneText.DIALOGUES: [
                'Whispers of the Hill: The wind whispers softly, as if carrying secrets from generations past. "You have chosen a path less traveled, seeker. The hill holds the keys to knowledge, but its gifts come with a price."'
            ],
        },
        "choice": {},
        "continue": (True, "Solve altar puzzle"),
    },
    {
        "name": "Solve altar puzzle",
        "text": {
            SceneText.NARRATIVES: [
                "Before you lies the ancient stone altar, its surface adorned with cryptic carvings that seem to tell a tale of forgotten rites and mystical powers. The symbols are arranged in an intricate pattern, an enigma waiting to be unraveled. As you approach, the air tingles with a heightened sense of anticipation, as if the woods itself is watching, waiting for your next move."
            ],
            SceneText.DIALOGUES: [
                'Whispers of the Carvings: Faint whispers emanate from the carvings, each symbol holding a voice of its own. "Decipher the language of the stones, seeker, and the path forward shall be revealed."',
                "Ancient Echoes: The air around the altar hums with the echoes of ancient incantations. The symbols seem to shift, their meaning dancing just beyond the grasp of understanding.",
            ],
        },
        "choice": {},
        "continue": (True, "Unlock secret passage"),
    },
    {
        "name": "Unlock secret passage",
        "text": {
            SceneText.NARRATIVES: [
                "Upon successfully solving the puzzle, a subtle vibration courses through the altar, and the air is charged with a newfound energy. The forest, as if acknowledging your accomplishment, seems to shift, revealing a passage that leads deeper into the heart of the forbidden realm.",
                "As you step through the unveiled pathway, the whispers of the ancient trees accompany you, and the journey into the unknown continues.",
            ]
        },
        "choice": {},
        "continue": (True, "Encounter Ancient Guardian 1"),
    },
    {
        "name": "Encounter Ancient Guardian 1",
        "text": {
            SceneText.NARRATIVES: [
                "The secret passage leads you deeper into the heart of the whispering woods, where the air grows thick with an otherworldly presence. The path twists and turns, revealing hidden chambers and ancient murals that seem to chronicle the history of the mystical realm. As you venture forth, the passage opens into a vast cavern, its depths cloaked in an eerie half-light.",
                "Suddenly, the silence is shattered by the awakening of an ancient guardian. A creature, part creature, part ethereal being, materializes before you. Its eyes, glowing with an ancient wisdom, lock onto yours, and the guardian utters a warning that echoes through the cavern.",
            ],
            SceneText.DIALOGUES: [
                "Guardian's warning: \"You trespass in the sacred lair of the forest's guardian. Face the consequences of your intrusion, seeker.\""
            ],
        },
        "choice": {},
        "continue": (True, "Encounter Ancient Guardian 2"),
    },
    {
        "name": "Encounter Ancient Guardian 2",
        "text": {
            SceneText.NARRATIVES: [
                "The cavern walls tremble as the guardian summons an enchanted barrier, sealing the exit behind you. Panic sets in as you realize that escape is the only option. The cavern seems to constrict, its walls closing in as the guardian's formidable presence looms ever closer. In the dim half-light, you make a split-second decision, realizing that escape is the only option. Your breath quickens, heartbeat pounding in your ears as you dash into the labyrinthine passages of the cavern.",
                "The air crackles with an ancient energy, and the luminous eyes of the guardian pierce through the darkness, fixing onto your fleeing figure. The guardian, a formidable presence, begins its relentless pursuit.",
            ]
        },
        "choice": {},
        "continue": (True, "Escape from Guardian's lair"),
    },
    {
        "name": "Escape from Guardian's lair",
        "text": {
            SceneText.NARRATIVES: [
                "As you sprint through the cavern, the path forks, offering a choice between two diverging routes. The dimly lit passages seem to stretch endlessly, and the choices are presented to you in the heat of the moment."
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "Go Left: The left path winds through narrow corridors, the sound of your footsteps reverberating against the cavern walls. The guardian follows, its echoing footsteps creating a haunting symphony.",
                "Go Right: Opting for the right path leads you through a series of twisting tunnels, the shadows playing tricks on your perception.",
            ],
        },
        "choice": {
            "1": "Escape from Guardian's lair - Go left",
            "2": "Escape from Guardian's lair - Go right",
        },
        "continue": (False, None),
    },
    {
        "name": "Escape from Guardian's lair - Go left",
        "text": {
            SceneText.NARRATIVES: [
                "The labyrinthine passages eventually converge, leading to a final sprint towards the exit. The guardian, relentless in its pursuit, is momentarily delayed by the complexities of the cavern's layout.",
                "As you burst into the open, the guardian's magical barrier dissipates, allowing you to escape the confines of the lair. The cavern's oppressive air is replaced by the cool breeze of the whispering woods. The woods, now calm, watches silently as you catch your breath. You stand at the edge of the cavern, chest heaving, the echoes of the guardian's footsteps fading away. The ancient guardian, bound by the sacred laws of the woods, retreats to its lair, and you are left to contemplate the next steps in your journey through the mysterious realm.",
            ]
        },
        "choice": {},
        "continue": (True, "Find abandoned path"),
    },
    {
        "name": "Escape from Guardian's lair - Go right",
        "text": {
            SceneText.NARRATIVES: [
                "The labyrinthine passages eventually converge, leading to a final sprint towards the exit. The guardian, relentless in its pursuit, is momentarily delayed by the complexities of the cavern's layout.",
                "As you burst into the open, the guardian's magical barrier dissipates, allowing you to escape the confines of the lair. The cavern's oppressive air is replaced by the cool breeze of the whispering woods. The woods, now calm, watches silently as you catch your breath. You stand at the edge of the cavern, chest heaving, the echoes of the guardian's footsteps fading away. The ancient guardian, bound by the sacred laws of the woods, retreats to its lair, and you are left to contemplate the next steps in your journey through the mysterious realm.",
            ]
        },
        "choice": {},
        "continue": (True, "Find abandoned path"),
    },
    {
        "name": "Study the map",
        "text": {
            SceneText.NARRATIVES: [
                "Choosing to focus on the ancient map in your hands, you meticulously follow the marked routes and symbols, navigating the intricate paths of the whispering woods. The map becomes a trusted guide, leading you through hidden groves, across babbling brooks, and beneath the ancient boughs of towering trees. The air resonates with a different energy, one guided by the calculated strokes of ink on parchment."
            ]
        },
        "choice": {},
        "continue": (True, "Find abandoned path"),
    },
    {
        "name": "Follow the melody",
        "text": {
            SceneText.NARRATIVES: [
                "Entranced by the haunting melody, you weave through the ancient trees, guided by the ethereal strains that seem to pull you deeper into the heart of the whispering woods.The foliage thickens, and the air becomes charged with a mystical energy as you follow the unseen path laid out by the enchanted song."
            ]
        },
        "choice": {},
        "continue": (True, "Find abandoned path"),
    },
    {
        "name": "Find abandoned path",
        "text": {
            SceneText.NARRATIVES: [
                "You pause, feeling a subtle shift in the air, and your intuition nudges you toward an unexplored direction. The abandoned path reveals itself gradually, a faint trail beneath the overgrown canopy. The air becomes charged with anticipation, as if the very trees are watching, acknowledging your presence.",
                "You tread cautiously, the overgrown foliage parting to unveil the hidden route. The ground beneath your feet feels different, carrying a weight of untold stories. As you walk along the abandoned path, there's a sense of entering a realm untouched by recent footsteps, a place where the wood's whispers are more pronounced. ",
            ]
        },
        "choice": {},
        "continue": (True, "Spot glowing object with peculiar markings"),
    },
    {
        "name": "Spot glowing object with peculiar markings",
        "text": {
            SceneText.NARRATIVES: [
                "As you traverse the abandoned path, a soft glow catches your eye. A few steps ahead, nestled among the overgrown roots of a towering tree, you discover a small, radiant object with peculiar markings. It emits a gentle hum, as if inviting you to unravel the mysteries it holds.",
                "Approaching the glowing object, you notice the peculiar markings on its surface. The symbols seem to dance in response to the the subtle energy shivering in the air and the forest seems to hold its breath.",
            ],
            SceneText.DIALOGUES: [
                'The Object\'s Whisper: The glowing object emits a melodic hum, as if sharing a tale with the seeker. "Bearer of the map, seeker of the forgotten, you have uncovered a key to the secrets that linger in the shadows."'
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Ignore object",
                "[2] - Check out object",
            ],
        },
        "choice": {"1": "Ignore object", "2": "Check out object"},
        "continue": (False, None),
    },
    {
        "name": "Ignore object",
        "text": {
            SceneText.NARRATIVES: [
                "Choosing to ignore the glowing object, your attention shifts to the surroundings. The woods, draped in an ancient silence, seems to beckon you further along the abandoned path. As you resume your journey, a faint trail reveals itself, a subtle whisper in the language of the trees."
            ]
        },
        "choice": {},
        "continue": (True, "Follow faint trail"),
    },
    {
        "name": "Follow faint trail",
        "text": {
            SceneText.NARRATIVES: [
                "As you tread upon the faint trail, a sense of curiosity blooms within you. Shadows play upon the foliage as you venture deeper into the abandoned area. The woods, a canvas of shifting shades, weaves a tapestry of intrigue, inviting you to unravel the secrets concealed within the elusive corridors."
            ]
        },
        "choice": {},
        "continue": (True, "Reach hidden cave with split paths"),
    },
    {
        "name": "Check out object",
        "text": {
            SceneText.NARRATIVES: [
                "As you approach the glowing object, a soft hum resonates through the air, and the peculiar markings on its surface seem to dance in response, a sudden realization dawns – thewoods, with all its mysteries, is offering you passage to realms beyond imagination. A gentle touch sends ripples across its radiant glow, and in an instant, the woods comes alive with a surge of mystical energy. The air shivers with anticipation, and before you can comprehend the unfolding events, a swirling vortex materializes around the object."
            ]
        },
        "choice": {},
        "continue": (True, "Sucked into vortex"),
    },
    {
        "name": "Sucked into vortex",
        "text": {
            SceneText.NARRATIVES: [
                "Before you can retreat, the vortex gains strength, and the irresistible pull draws you in. In an instant, the world around you blurs and distorts as the vortex envelops you. The forest's symphony of rustling leaves and distant whispers fades, replaced by the disorienting whirl of inter-dimensional energies. You are engulfed in a kaleidoscope of colors and sensations, as if hurtling through the very essence of existence.",
                "In an instant, the world around you blurs and distorts as the vortex envelops you. The forest's symphony of rustling leaves and distant whispers fades, replaced by the disorienting whirl of inter-dimensional energies. You are engulfed in a kaleidoscope of colors and sensations, as if hurtling through the very essence of existence.",
            ],
            SceneText.DIALOGUES: [
                'Whispers of the Vortex: The forest seems to whisper as the vortex emerges, its spiraling energy pulling at the fabric of reality. "Bearer of curiosity, seeker of the unknown, you have unlocked the gateway to realms untold."'
            ],
        },
        "choice": {},
        "continue": (True, "Reach magical grove"),
    },
    {
        "name": "Reach magical grove",
        "text": {
            SceneText.NARRATIVES: [
                "As the swirling vortex dissipates, you find yourself standing in the heart of a magical grove. The air is infused with an enchanting glow, and the foliage shimmers with hues unseen in the mortal realm. The trees, ancient sentinels of this mystical sanctuary, stretch their branches towards a sky painted in ethereal colors. The colors of the grove, vibrant and surreal, evoke a sense of wonder, a living spell, casted by the forces that govern this otherworldly haven."
            ],
            SceneText.DIALOGUES: [
                'Whispers of the Grove: The grove seems to whisper secrets of ages past, as if the very trees are keepers of ancient knowledge. "Welcome, seeker, to the heart of the magical realm. Here, the boundaries between worlds blur, and the very air is alive with enchantment."'
            ],
        },
        "choice": {},
        "continue": (True, "Path ahead blocked by ancient trees"),
    },
    {
        "name": "Path ahead blocked by ancient trees",
        "text": {
            SceneText.NARRATIVES: [
                "As you venture deeper into the grove, ancient trees materialize, forming an impenetrable barrier across your path. Their gnarled roots and twisted branches seem to converge, creating an enchantment that obstructs any attempt to move forward. The barrier is a testament to the grove's protective magic. The seeker must unravel the threads of nature's enchantment, proving their understanding of the delicate balance that sustains this magical sanctuary."
            ],
            SceneText.DIALOGUES: [
                "Ancient Guardian's Whispers: The ancient trees, guardians of the magical grove, seem to communicate through rustling leaves and creaking branches. \"Bearer of the vortex's touch, only those attuned to the essence of this realm may pass beyond this threshold.\""
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Continue ahead",
                "[2] - Try to find a way out",
            ],
        },
        "choice": {
            "1": "Continue ahead",
            "2": "Try to find a way out",
        },
        "continue": (False, None),
    },
    {
        "name": "Continue ahead",
        "text": {
            SceneText.NARRATIVES: [
                "Undeterred by the ancient trees blocking the path, you decide to press forward, driven by an unyielding determination to explore the magical grove. The air crackles with anticipation as you confront the enchanted barrier. The trees stand tall and unyielding, their branches intertwined like an intricate puzzle. The trees, though rooted in centuries of wisdom, acknowledge your boldness. Whispers of admiration and curiosity drift through the grove, carried on the breeze that weaves through the foliage."
            ]
        },
        "choice": {},
        "continue": (True, "Decipher order of words tress are whispering"),
    },
    {
        "name": "Decipher order of words tress are whispering",
        "text": {
            SceneText.NARRATIVES: [
                "As you approach the barrier, the trees' whispers become more pronounced, forming a melodic symphony of ancient words. However, the words are not spoken in a language known to mortals; instead, they seem to transcend the boundaries of comprehension. You soon realize that the key to parting the trees lies in deciphering the order of these mystical words. The air is filled with a cascade of whispers, each word a puzzle piece in the language of the magical grove. You, surrounded by the ethereal symphony, must attune their senses to the subtle nuances of the enchanted words. As the seeker engages with the enchanted words, the magical grove watches, its ancient guardians observing the seeker's quest to unravel the mysteries woven into the very fabric of the realm."
            ]
        },
        "choice": {},
        "continue": (True, "Trees part"),
    },
    {
        "name": "Trees part",
        "text": {
            SceneText.NARRATIVES: [
                "As you decipher the order of the enchanted words, the trees seem to part, their branches creating a pathway through the barrier. The trees, guardians of the magical grove, acknowledge your understanding of the mystical language, and the barrier yields to your mastery of its secrets. The grove, now a tapestry of magical hues, seems to applaud your determination. The ancient trees, now your guides, watch as you venture deeper into the heart of the enchanted sanctuary, eager to unfold the secrets that lie ahead."
            ],
            SceneText.DIALOGUES: [
                "Echoes of Success: The grove seems to echo with the whispers of success as the enchanted barrier yields to your comprehension. The ancient trees, their branches parting like curtains, invite you to step beyond the threshold and continue your journey."
            ],
        },
        "choice": {},
        "continue": (True, "Find a small pathway"),
    },
    {
        "name": "Try to find a way out",
        "text": {
            SceneText.NARRATIVES: [
                "Faced with the imposing barrier of ancient trees, you choose a different approach. Rather than attempting to force your way forward, you decide to explore the perimeter of the enchanted grove in search of an alternate path. The air, thick with the essence of magic, becomes a guide as you navigate the mystical sanctuary. The grove seems to acknowledge your decision with a gentle rustle of leaves."
            ]
        },
        "choice": {},
        "continue": (True, "Find a small pathway"),
    },
    {
        "name": "Find a small pathway",
        "text": {
            SceneText.NARRATIVES: [
                "As you navigate the perimeter of the enchanted grove, your senses become finely attuned to the mystical details woven into the fabric of the forest. The dance of dappled light, the faint yet alluring melody playing on nature's strings, and a discernible shift in the energy of the grove reveal themselves as silent guides. These subtle cues beckon you toward a concealed trail, winding its way through the ancient trees. The air becomes charged with anticipation as you step onto the concealed trail, leaving the imposing trees behind."
            ],
            SceneText.DIALOGUES: [
                "Nature's Invitation: The grove seems to extend an unspoken invitation as you follow the whimsical play of light and shadow. It's as if the very essence of nature is guiding your steps, revealing a hidden narrative written in the language of the enchanted realm.",
                "Melody of Discovery: The faint melody, ethereal and captivating, floats through the air like a muse guiding a poet's pen. It whispers secrets of the concealed trail, inviting you to uncover the harmonious symphony of the grove's untouched corners.",
            ],
        },
        "choice": {},
        "continue": (True, "Path blocked by Celestial guardian"),
    },
    {
        "name": "Path blocked by Celestial guardian",
        "text": {
            SceneText.NARRATIVES: [
                "As you tread further along the concealed trail, a celestial hush descends upon the enchanted grove. The air crackles with an otherworldly energy, and the soft glow that once guided your way now intensifies, casting shadows that dance with ethereal luminescence. Before you stands a celestial guardian, a majestic being adorned in celestial light, its form radiant and enigmatic.",
                "The celestial guardian, its luminous form casting a celestial glow over the trail, gestures in a way that suggests a challenge. An ethereal barrier materializes, blocking your path forward. The guardian's eyes, sparkling with the light of distant galaxies, seem to pose a question that transcends spoken language.",
            ],
            SceneText.DIALOGUES: [
                "Cosmic Riddle:_ The guardian's voice, a melodic resonance of cosmic proportions, poses a riddle that reverberates through the grove. The seeker feels the weight of the celestial puzzle, a challenge that goes beyond earthly understanding."
            ],
        },
        "choice": {},
        "continue": (True, "Answer riddle given by Guardian"),
    },
    {
        "name": "Answer riddle given by Guardian",
        "text": {
            SceneText.NARRATIVES: [
                "The celestial guardian, its form radiant with the light of distant stars, presents a cosmic riddle that hangs in the air like a constellation awaiting interpretation. The riddle reverberates through the grove like celestial music, and you senses the weight of the cosmic puzzle. The guardian's gaze, a cascade of starlight, waits for your response. The grove, holding its breath in celestial reverence, becomes a witness to your challenge."
            ],
            SceneText.DIALOGUES: [
                'Celestial Riddle:_ The guardian\'s voice resonates with the harmonies of the cosmos as it presents the riddle. "In the realm of eternity, I dance with the night, yet every dawn, I fade from sight. What am I, seeker of the earthly domain?"'
            ],
        },
        "choice": {},
        "continue": (True, "Glowing vertex reappears"),
    },
    {
        "name": "Glowing vertex reappears",
        "text": {
            SceneText.NARRATIVES: [
                "As you formulate an answer that resonates with the dance of the cosmos, the guardian's eyes, sparkling with cosmic approval, convey an acknowledgment of your insight. In response to the guardian's approval, a glowing, swirling vortex materializes once more, like a cosmic doorway opening in the fabric of the enchanted grove. In an instant, you are enveloped in the swirling vortex, carried away by the currents of cosmic energies. The celestial guardian's final gaze follows your departure, and as the vortex dissipates, the grove returns to its mystical stillness."
            ],
            SceneText.DIALOGUES: [
                "Cosmic Convergence:_ The guardian's luminous form seems to blend with the cosmic energies, resonating in harmony with the seeker's insight. \"Seeker, your understanding of the celestial dance is acknowledged. Return to the earthly realm through the vortex, and carry the wisdom of the cosmos with you.\""
            ],
        },
        "choice": {},
        "continue": (True, "Reach hidden cave with split paths"),
    },
    {
        "name": "Reach hidden cave with split paths",
        "text": {
            SceneText.NARRATIVES: [
                "As you travel along the faint trail, the air becomes thick with ancient magic. Suddenly, a hidden cave reveals itself, its entrance veiled by vines and moss. The scent of earth and mystery lingers as you step into the cavern's cool embrace. Inside, the cave splits into two paths, each glistening with glowing crystals, beckoning you with an air of undiscovered secrets. As the left and right passages extend into darkness, each concealing its own mysteries and challenges, your decision next will shape the unfolding narrative in the heart of the whispering woods."
            ],
            SceneText.DIALOGUES: [
                "Cave's Whispers: The cave seems to murmur with the voices of unseen guardians, sharing tales of diverging paths that lead to unexplored realms. The air within the cavern becomes a repository of forgotten stories, inviting you to choose your destiny."
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Follow the left path",
                "[2] - Embark on the right path",
            ],
        },
        "choice": {
            "1": "Follow the left path",
            "2": "Embark on the right path",
        },
        "continue": (False, None),
    },
    {
        "name": "Embark on the right path",
        "text": {
            SceneText.NARRATIVES: [
                "The right path unfolds before you with a grace that seems to harmonize with the very heartbeat of the earth. The air becomes charged with an energy that speaks of unseen wonders awaiting your discovery."
            ]
        },
        "choice": {},
        "continue": (True, "Reach end of cave"),
    },
    {
        "name": "Reach end of cave",
        "text": {
            SceneText.NARRATIVES: [
                "As you tread the right path through the winding corridors of the hidden cave, the air becomes cooler, and the glow of crystals intensifies, illuminating your way. As you navigate the twists and turns, the right path leads you deeper into the heart of the cave. With each step, anticipation builds, and soon, you find yourself at the end of the cave."
            ],
            SceneText.DIALOGUES: [
                "Subtle Echoes: The cave walls seem to echo with the soft resonance of your footsteps. Subtle whispers of ancient secrets brush against your senses, guiding you as you venture further into the mysterious depths."
            ],
        },
        "choice": {},
        "continue": (True, "Find a boat"),
    },
    {
        "name": "Find a boat",
        "text": {
            SceneText.NARRATIVES: [
                "Where the rocky floor gives way to a small underground shore, in the dim light, a remarkable discovery awaits—a boat, patiently resting on the subterranean waters, its silhouette framed by the gentle glow of crystals. The boat, crafted from ancient wood and adorned with symbols that seem to shimmer, exudes a quiet serenity as it floats upon the subterranean waters, sitting silently as if holding the stories of a thousand voyages. The air carries a sense of expectancy, inviting you to explore its secrets."
            ]
        },
        "choice": {},
        "continue": (True, "Solve puzzle"),
    },
    {
        "name": "Solve puzzle",
        "text": {
            SceneText.NARRATIVES: [
                "As you stand by the boat at the end of the cave, a subtle hum emanates from its wooden frame. It seems as though the vessel is waiting for something -- an acknowledgment, a sign. Upon closer inspection, you notice a series of symbols intricately carved into the boat's surface. They form a puzzle, a cryptic dance of shapes that holds the key to bringing the boat to life. The symbols etched into the boat's surface seem to pulse with a faint energy. They hold the essence of the cave's mysteries, and the hum intensifies as if urging you to decipher the ancient code that binds the boat to the subterranean waters."
            ],
            SceneText.DIALOGUES: [
                "Cryptic Whispers: The cave, with its echoes of forgotten tales, seems to whisper secrets of the symbols' meanings. The air becomes charged with an unseen force, encouraging you to engage with the puzzle and unlock the boat's dormant magic.",
                "The Boat's Song: As you gaze upon the symbols, a melodic hum resonates from the boat. It's as if the vessel itself is singing a cryptic song, inviting you to join in and become a part of the subterranean harmony that lingers in the cavern's depths.",
            ],
        },
        "choice": {},
        "continue": (True, "Boat engine starts"),
    },
    {
        "name": "Boat engine starts",
        "text": {
            SceneText.NARRATIVES: [
                "With the final placement of the symbols, a surge of energy ripples through the boat. The hum transforms into a melodic symphony, and the once-dormant vessel now pulses with life. The symbols, once enigmatic, now glow with a soft luminescence, as if acknowledging your unravelling of their secrets. With a subtle shiver, the boat is now ready to navigate the subterranean waters and unveil the secrets that lie beyond the cave's threshold."
            ],
            SceneText.DIALOGUES: [
                "Echoes of Enchantment: The cavern echoes with the harmonious resonance of the awakened boat. The melodic vibrations create a sacred dance between the seeker, the symbols, and the vessel itself, as if an unspoken connection has been forged between the earthly realm and the subterranean waters."
            ],
        },
        "choice": {},
        "continue": (True, "Cross the river"),
    },
    {
        "name": "Follow the left path",
        "text": {
            SceneText.NARRATIVES: [
                "The left path leads you through a series of chambers adorned with crystalline formations and mystical symbols. The air becomes charged with anticipation, and as you move deeper, the crystalline glow intensifies, casting intricate patterns on the walls."
            ]
        },
        "choice": {},
        "continue": (True, "Discover ancient monument"),
    },
    {
        "name": "Discover ancient monument",
        "text": {
            SceneText.NARRATIVES: [
                "Suddenly, the corridor opens into a vast chamber adorned with ancient symbols and formations. At the heart of the chamber stands an imposing monument, its surface etched with a language of ages long past, symbols that seem to tell tales of forgotten civilizations and mystical rites. The air becomes thick with the weight of history, humming with a resonance that invites you to decipher the secrets embedded in the ancient stone."
            ],
            SceneText.DIALOGUES: [
                "Whispers of the Ancients: The chamber seems to pulse with an ancient energy as you approach the monument. Whispers, soft and ethereal, echo through the vast space, revealing the untold stories engraved into the stone."
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Examine the carvings",
                "[2] - Ignore the monument",
            ],
        },
        "choice": {
            "1": "Examine the carvings",
            "2": "Ignore the monument",
        },
        "continue": (False, None),
    },
    {
        "name": "Ignore the monument",
        "text": {
            SceneText.NARRATIVES: [
                "Choosing to ignore the ancient monument, you continue along the path, leaving the vast chamber behind. The glow of crystals guides your way, and the whispers of the cave fade as you move deeper into the labyrinthine corridors. The soft hum of the crystals seems to weave a lullaby, creating a serene ambiance as you continue along the left path. The air, though charged with subterranean energy, becomes more tranquil as you distance yourself from the imposing stone structure."
            ]
        },
        "choice": {},
        "continue": (True, "Reach end of cave"),
    },
    {
        "name": "Examine the carvings",
        "text": {
            SceneText.NARRATIVES: [
                "Choosing to examine the carvings on the ancient monument, you approach the imposing stone structure with a sense of curiosity. The symbols, weathered by time, reveal intricate carvings that seem to hold the key to the subterranean mysteries, vibrating with an otherworldly energy that invites you to unlock the secrets hidden within the stone.. As you study the symbols, the air in the chamber becomes charged with an ancient energy, and the whispers of the cave intensify."
            ]
        },
        "choice": {},
        "continue": (True, "Encounter mysterious mist"),
    },
    {
        "name": "Encounter mysterious mist",
        "text": {
            SceneText.NARRATIVES: [
                "As you immerse yourself in examining the ancient carvings on the monument, a mysterious mist begins to materialize around you. The air becomes thick with an otherworldly presence, and the soft glow of the crystals dims as the mist envelops the chamber. The mist creates a veil that shrouds the path ahead, concealing what lies beyond. Its touch is cool and enigmatic, exuding an aura of secrets waiting to be unveiled, tempting you with the allure of the unknown that lies on the other side."
            ],
            SceneText.DIALOGUES: [
                "Whispers in the Mist: The mist seems to carry echoes of ancient whispers, beckoning you into its ethereal embrace. As it swirls around the chamber, the symbols on the monument take on a spectral quality, creating an illusionary dance of forgotten tales."
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Enter the mist",
                "[2] - Try to turn back",
            ],
        },
        "choice": {"1": "Enter the mist", "2": "Try to turn back"},
        "continue": (False, None),
    },
    {
        "name": "Enter the mist",
        "text": {
            SceneText.NARRATIVES: [
                "Rather than attempting to find an escape route, a surge of courage takes hold. With determination in your heart, you bravely step into the swirling embrace of the enigmatic fog. In the heart of the mist, you find yourself in a realm that transcends the boundaries of the visible. The air is charged with a palpable energy, and the mist seems to respond to the your presence, parting before you as if leading the way through an unseen path."
            ]
        },
        "choice": {},
        "continue": (True, "Stumble upon enchanted glade"),
    },
    {
        "name": "Stuble upon enchanted glade",
        "text": {
            SceneText.NARRATIVES: [
                "As you continue through the mist, a subtle change occurs in the surroundings. The air becomes infused with a gentle luminosity, and the mist begins to part, revealing an enchanted glade bathed in a soft, otherworldly glow. The glade is crowned by a canopy of luminescent leaves, creating a celestial ambiance that filters the mist into a gentle, iridescent glow. Sunlight seems to penetrate the mist, casting a dappled radiance over the enchanted realm. The ground is carpeted with vibrant moss, and ethereal flowers bloom in radiant hues that seem to defy the muted tones of the mist. At the center of the glade, a crystalline pool reflects the surrounding beauty. The waters ripple with a serene melody, inviting you to approach and peer into its depths, where secrets may lie hidden beneath the surface."
            ]
        },
        "choice": {},
        "continue": (True, "Meet fairy"),
    },
    {
        "name": "Meet fairy",
        "text": {
            SceneText.NARRATIVES: [
                'As you marvel at the enchanting glade, a melodic giggle resonates through the air. From within the foliage emerges a tiny, radiant figure—a fairy with delicate wings that shimmer like spun silver. The fairy hovers in the air, her presence exuding a sense of benevolence and magic. With a twinkle in her eyes, the fairy introduces herself with a graceful twirl, " I am Caelia, guardian of the enchanted glade. In this glade, secrets are whispered by the breeze and hidden in the dance of light. The enchanted realms hold answers for those who dare to seek. Ask, and you shall receive guidance."'
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Ignore the fairy",
                "[2] - Interact with the fairy",
            ],
        },
        "choice": {"1": "Ignore the fairy", "2": "Interact with the fairy"},
        "continue": (False, None),
    },
    {
        "name": "Interact with the fairy",
        "text": {
            SceneText.NARRATIVES: [
                "Intrigued by the fairy's ethereal presence and the allure of the enchanted glade, you decide to interact with Caelia. You approach the guardian fairy with a respectful nod, acknowledging the magical atmosphere that surrounds the both of you. Caelia responds with a gracious nod, offering blessings of the glade to you."
            ]
        },
        "choice": {},
        "continue": (True, "Journey to ancient ruin"),
    },
    {
        "name": "Journey to ancient ruin",
        "text": {
            SceneText.NARRATIVES: [
                "Embracing the guidance of Caelia, you follow her lead through the enchanted glade. As you venture deeper, the mist seems to part, unveiling a hidden path that leads to a realm untouched by the passage of time—the ancient ruins, a place where the mysteries of the past converge with the magic of the present. With a twirl in the air, Caelia beckons you forward. She mentioned a central chamber within the ruins—a nexus of ancient power where you may find the answer you seek. "
            ]
        },
        "choice": {},
        "continue": (True, "Uncover ancient artifact"),
    },
    {
        "name": "Uncover ancient artifact",
        "text": {
            SceneText.NARRATIVES: [
                "Within the heart of the ancient ruins, you navigate the labyrinthine corridors, your every step echoing through the silent stones. Guided by the ethereal glow of Caelia's presence, you arrive at the central chamber—a sacred enclave where time itself seems to hold its breath. Pillars, once towering in grandeur, now stand as weathered sentinels, their surfaces adorned with intricate carvings that tell tales of a civilization obscured by the veil of ages. Cracks trace the stories of time, revealing the fragility of once-imposing structures. The walls are adorned with murals that withstand the erosion of time. Fading pigments depict scenes of mystical rituals, celestial alignments, and guardians that seem to transcend the boundary between the earthly and the divine. In the midst of this silent sanctuary, your gaze fall upon a pedestal, weathered by the passage of time. It cradles the ancient artifact—an enigmatic object adorned with intricate symbols and emanating a subtle, pulsating energy that resonates with the seeker's very being."
            ],
            SceneText.DIALOGUES: [
                "Lost Whispers: The air in the central chamber is thick with the hushed echoes of the past. Faint whispers linger in the recesses, as if the very walls retain memories of the bygone era. You stand as an intruder in a sanctum of forgotten tales."
            ],
        },
        "choice": {},
        "continue": (True, "Decrypt ancient language"),
    },
    {
        "name": "Decrypt ancient language",
        "text": {
            SceneText.NARRATIVES: [
                "As you stand before the ancient artifact within the central chamber, you realize that unravelling its mysteries requires more than a mere touch—it demands the deciphering of an ancient language etched into its surface. The symbols, enigmatic and intricate, appear to conceal the wisdom of an era long past. Each stroke on the surface seems to carry the weight of forgotten tales and unspoken knowledge. As you examine the symbols, a subtle pulsating energy emanates from the artifact. It responds to your gaze, as if inviting you to delve into the heart of its inscriptions and unlock the dormant secrets held within. Undeterred, you prepares to embark on the challenging task of deciphering the arcane language."
            ]
        },
        "choice": {},
        "continue": (True, "Decode symbols for clues"),
    },
    {
        "name": "Decode symbols for clues",
        "text": {
            SceneText.NARRATIVES: [
                "You, equipped with an inquisitive mind, begin the intricate process of deciphering the ancient language. By scrutinizing the glyphs, you seek patterns and connections that may shed light on the meaning concealed within the stone. As you meticulously decodes the symbols, patterns begin to emerge. Clues embedded within the carvings hint at the ancient civilization's rituals, celestial alignments, and the role of the guardians. Your efforts slowly unveil the narrative woven into the artifact's surface."
            ]
        },
        "choice": {},
        "continue": (True, "Discover a hidden bridge"),
    },
    {
        "name": "Discover a hidden bridge",
        "text": {
            SceneText.NARRATIVES: [
                "As you successfully decipher the ancient language on the artifact, the symbols on the surface begin to resonate, aligning in harmony as the last remnants of the forgotten language reveal their secrets. The artifact emanates a vibrant pulse of energy, rippling through the air and creating an otherworldly glow that bathes the entire chamber. Suddenly, a low hum fills the central chamber, and you watch in awe as the stone beneath your feet begins to shift. Sections of the chamber floor seamlessly rearrange, unveiling a hidden bridge.",
                "As you step onto the revealed bridge, a soft glow emanates from beneath your feet, guiding the way across the ancient walkway, and towards the wetlands, where murky waters challenge the path ahead. Meanwhile, Caelia, the guardian fairy, flutters in delight, her wings aglow with the newfound energy. Her melodic laughter resonates through the chamber, echoing the joyous revelation of the your success. She then gave you a wink, accompanied by a tiny wave of hands before she fades away with the otherworldly glow that filled the chamber moments earlier.",
            ]
        },
        "choice": {},
        "continue": (True, "Cross the river"),
    },
    {
        "name": "Cross the river",
        "text": {
            SceneText.NARRATIVES: [
                "The wetlands stretch out in all directions, a tapestry of reeds, water lilies, and meandering streams. As you approach the wetlands, a symphony of nature's sounds fills the air. Chirping insects, the distant call of unseen creatures, and the rustling of wetland foliage create a melodic backdrop to your journey as you navigate through the embrace of nature's lush vegetation. As you near the end of the wetlands, you are finally able to stand on solid ground of the whispering woods, having successfully traversed the wetlands that marked the final frontier of your mystical journey."
            ]
        },
        "choice": {},
        "continue": (True, END_SCENE),
    },
    {
        "name": "Ignore the fairy",
        "text": {
            SceneText.NARRATIVES: [
                "Despite the fairy's enchanting presence and the allure of the magical glade, you, driven by an unyielding sense of determination, decides to ignore Caelia's offer of guidance. With a nod of gratitude, you forge ahead on your chosen path, weaving through the glade without allowing the allure of fairy magic to sway your purpose. Caelia's melodic laughter fades into the background as you distance yourself from her. The glade, once alive with the Caelia's presence, now returns to a tranquil state, with only the gentle rustle of leaves and the distant murmur of the mystic pool breaking the stillness."
            ]
        },
        "choice": {},
        "continue": (True, "Encounter old cabin"),
    },
    {
        "name": "Try to turn back",
        "text": {
            SceneText.NARRATIVES: [
                "Guided by an instinctual sense of exploration, you opt to turn back from the mysterious mist, retracing your steps through the labyrinthine corridors of the hidden cave. The glow of crystals guides your way as you navigate the familiar passages."
            ]
        },
        "choice": {},
        "continue": (True, "Stumble upon hidden path"),
    },
    {
        "name": "Stumble upon hidden path",
        "text": {
            SceneText.NARRATIVES: [
                "As you backtrack, a subtle shift in the air catches your attention. Your instincts lead you to a concealed trail, hidden among the intricacies of the cave's walls. Embracing the unexpected turn of events, you embark on the concealed trail. The air seems charged with anticipation, and each twist and turn of the hidden passage opens up new chambers adorned with formations that seem to breathe with the essence of ages long past."
            ],
            SceneText.DIALOGUES: [
                "A Whispering Breeze: The air along the concealed trail carries a whispered breeze, as if the very walls of the cave are sharing secrets. The unseen forces seem to beckon you deeper, leading you away from the known into a realm where mysteries intertwine with every step."
            ],
        },
        "choice": {},
        "continue": (True, "Discover cryptic note"),
    },
    {
        "name": "Discover cryptic note",
        "text": {
            SceneText.NARRATIVES: [
                "You notice a subtle glimmer ahead. Upon closer inspection, you discover a small alcove nestled within the cave's walls. Within the alcove lies a weathered piece of parchment, a cryptic note that seems to have withstood the test of time. As you delve into the cryptic note, its symbols and markings begin to align with a rhythm only a seeker can comprehend. The ancient language on the parchment unveils itself, revealing a message that speaks of hidden chambers and an old cabin concealed."
            ],
            SceneText.DIALOGUES: [
                "The Whispers of the Note: As you unfold the cryptic note, the cave seems to hold its breath, as if eager to reveal the secrets penned on the aged parchment. The whispers of the subterranean sanctuary become more pronounced, echoing in harmony with the enigmatic message.",
                "An Ancient Correspondence: The cryptic note, though weathered by time, emanates an ancient aura. Its symbols and markings appear to be a form of correspondence from an era long past, inviting you to decipher the encoded message and unravel the narrative woven into the parchment.",
            ],
        },
        "choice": {},
        "continue": (True, "Encounter old cabin"),
    },
    {
        "name": "Encounter old cabin",
        "text": {
            SceneText.NARRATIVES: [
                "As you get closer to the heart of the subterranean depths, you find yourself standing before the entrance to a hidden chamber. The air within seems to ripple with the echoes of the past, and the glow of crystals intensifies, emphasizing the significance of the moment. Stepping into the chamber, you discover the old cabin—a silent witness to the tales of yesteryears, tucked away in a sanctuary guarded by the subterranean realm. The old cabin, though weathered by the passage of time, stands as a testament to a forgotten era. Its wooden walls bear the scars of age, and the entrance beckons, inviting you to step into a living relic from the past concealed within the subterranean depths."
            ],
            SceneText.DIALOGUES: [
                "Whispers of Yesteryears:_ The chamber echoes with the whispers of bygone eras, as if the walls of the cave harbor the stories of those who once sought refuge within the old cabin. The air within the chamber is thick with the scent of aged wood and the warmth of forgotten memories."
            ],
        },
        "choice": {},
        "continue": (True, "Investigate cabin"),
    },
    {
        "name": "Investigate cabin",
        "text": {
            SceneText.NARRATIVES: [
                "With the old cabin before you, a sense of anticipation hangs in the air. The wooden door, weathered and worn, creaks open as you cautiously step inside. The timbers creak, whispering tales of the countless visitors who sought refuge within its walls. Dust dances in the glow of crystals as you step into a space that seems frozen in a bygone era, as if the past has seeped into the very walls. As you investigate the cabin, the past seems to come alive.  It's as if the very air within holds the echoes of conversations, laughter, and perhaps even the solemn whispers of long-forgotten secrets. The past and present converge in a timeless dance. Each object, each corner, whispers tales of those who sought refuge in this concealed haven."
            ]
        },
        "choice": {},
        "continue": (True, "Find distress flare"),
    },
    {
        "name": "Find distress flare",
        "text": {
            SceneText.NARRATIVES: [
                "Amidst the relics of the old cabin, your eyes catch a glint in a dark corner. As you investigate further, you uncover a forgotten storage compartment. Within it lies a distress flare, its red casing standing out in stark contrast to the muted tones of the cabin. The distress flare, nestled among forgotten possessions, seems like a relic from a time when this cabin served as a refuge. Its vibrant red casing suggests a tool meant for urgent communication, evoking questions about the events that unfolded within the subterranean depths."
            ]
        },
        "choice": {},
        "continue": (True, "Meet rescue team"),
    },
    {
        "name": "Meet rescue team",
        "text": {
            SceneText.NARRATIVES: [
                "With the distress flare in hand, you decide to utilize its potential, recognizing it as a tool that can bridge the gap between the subterranean depths and the surface world. As you ignite the flare, its vivid red glow fills the chamber, casting an eerie yet captivating light on the old cabin's timeworn interior. The glow of the flare becomes a beacon that cuts through the darkness, signalling not only your presence but also the urgency of your situation. As the radiant glow of the distress flare permeates the hidden chamber, a distant rumble accompanied by voices that grow louder with each passing moment. The voices draw nearer, and the language spoken is one of familiarity—a rescue team, their words laced with concern and purpose.",
                "As the rescue team's footsteps draw near, a subtle shift in the atmosphere envelops the hidden cave. The woods beyond the cave seems to sigh, the once vibrant glow of crystals dims, and the eerie luminescence that danced upon timeworn walls begins to fade. It's as if everything in this whispering woods, aware of the approaching presence, desires to keep its secrets concealed. As the rescue team's flashlights pierce the darkness, the once enchanted woods now appears like any forgotten relic of the past. The rescue team leads you through the woods, the trees giving way to moonlit paths.",
            ]
        },
        "choice": {},
        "continue": (True, END_SCENE),
    },
    {
        "name": END_SCENE,
        "text": {
            SceneText.NARRATIVES: [
                "The journey, once fraught with mystery and danger, now transforms into a triumphant escape. As you step into the clearing, in a gesture of acknowledgment, the ancient trees in the woods seem to bow as you step beyond the woods' edge, emerging from the thrilling adventure into the embrace of the night, leaving the mysteries of the whispering woods behind. The woods, though left behind, becomes a part of a tale you will tell in the future—a forbidden adventure that unfolded amidst the shadows and secrets of a realm touched by magic, that will forever a lingering sense of wonder in your heart. As you step into the night, guided by the moon and the echoes of an unforgettable journey, the whispering woods continue to whisper its ancient secrets, awaiting for the next adventurer."
            ]
        },
        "choice": {},
        "continue": (False, None),
    },
]
