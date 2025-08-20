from pydantic import BaseModel
from rich.console import Console
from rich.pretty import Pretty

class Agent(BaseModel):
    name: str
    age: int
    height: int
    weight: int
    role: str
    clearance: int
    history: str
    status: bool

# Create an instance of your agent
agent = Agent(name="Kevin Artebury", age=52, height=69, weight=178, role="Field Operative", clearance=7, history="", status=False)
agent.history = "Kevin started as a soldier for the US military in the Second Gulf war. Not much is known of " \
                "his history prior to that. The CIA recruited him as a black ops operative after scouting him " \
                "from his days as a grunt. His official records are full of documents that have been heavily " \
                "redacted or classified to oblivion. Apparently, whatever the CIA had him doing, they don't want " \
                "any of it getting out. The agency recruited him early, and enjoyed 15 years of successful, " \
                "albeit unconventional missions. He was known for carrying nothing but a ball point click pen " \
                "and a digital wristwatch. He was a master at finding or crafting weapons in-situ. He developed" \
                "a reputation in the field as a quiet and effective operative. He worked alone even when " \
                "with a team. He would simply get to work, waiting on no one and completing each objective " \
                "one at a time until exfil. His last official assignment was completed 6 years ago. This was " \
                "also the last time anyone ever saw him. Now, disavowed by the agency, he has become a thing " \
                "of legend. Parents tell stories of Kevin to their little despots and criminal bosses to get " \
                "them to eat their broccoli. Most will only whisper his name. All fear it."
console = Console()
console.print(Pretty(agent.model_dump()))