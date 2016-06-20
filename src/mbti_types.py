"""MBTI types.

All profile descriptions from
http://www.myersbriggs.org/my-mbti-personality-type/mbti-
basics/the-16 -mbti-types.htm:
"""

from collections import namedtuple


AttributeMatrix = namedtuple('AttributeMatrix', ', '.join([
    'hp', 'mp',
    'strength', 'endurance',
    'defense', 'intelligence',
    'agility', 'charisma',
    'wisdom', 'willpower',
    'perception', 'luck'
]))


class MBTIType(object):
    """Base class."""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Istj(MBTIType):
    """Determine the response for this type, given another type.

    'Quiet, serious, earn success by thoroughness and dependability. Practical,
    matter-of-fact, realistic, and responsible. Decide logically what should be
    done and work toward it steadily, regardless of distractions. Take pleasure
    in making everything orderly and organized - their work, their home, their
    life. Value traditions and loyalty.'
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Isfj(MBTIType):
    """Determine the response for this type, given another type.

    Quiet, friendly, responsible, and conscientious. Committed and steady in
    meeting their obligations. Thorough, painstaking, and accurate. Loyal,
    considerate, notice and remember specifics about people who are important
    to them, concerned with how others feel. Strive to create an orderly and
    harmonious environment at work and at home.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Infj(MBTIType):
    """Determine the response for this type, given another type.

    Seek meaning and connection in ideas, relationships, and material
    possessions. Want to understand what motivates people and are insightful
    about others. Conscientious and committed to their firm values. Develop a
    clear vision about how best to serve the common good. Organized and
    decisive in implementing their vision.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Intj(MBTIType):
    """Determine the response for this type, given another type.

    Have original minds and great drive for implementing their ideas and
    achieving their goals. Quickly see patterns In external events and develop
    long-range explanatory perspectives. When committed, organize a job and
    carry it through. Skeptical and independent, have high standards of
    competence and performance - for themselves and others.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Istp(MBTIType):
    """Determine the response for this type, given another type.

    Tolerant and flexible, quiet observers until a problem appears, then act
    quickly to find workable solutions. Analyze what makes things work and
    readily get through large amounts of data to isolate the core of practical
    problems. Interested in cause and effect, organize facts using logical
    principles, value efficiency.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Isfp(MBTIType):
    """Determine the response for this type, given another type.

    Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's
    going on around them. Like to have their own space and to work within their
    own time frame. Loyal and committed to their values and to people who are
    important to them. Dislike disagreements and conflicts, do not force their
    opinions or values on others.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Infp(MBTIType):
    """Determine the response for this type, given another type.

    Idealistic, loyal to their values and to people who are important to them.
    Want an external life that is congruent with their values. Curious, quick
    to see possibilities, can be catalysts for implementing ideas. Seek to
    understand people and to help them fulfill their potential. Adaptable,
    flexible, and accepting unless a value is threatened.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Intp(MBTIType):
    """Determine the response for this type, given another type.

    Seek to develop logical explanations for everything that interests them.
    Theoretical and abstract, interested more in ideas than in social
    interaction. Quiet, contained, flexible, and adaptable. Have unusual
    ability to focus In depth to solve problems In their area of interest.
    Skeptical, sometimes critical, always analytical.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Estp(MBTIType):
    """Determine the response for this type, given another type.

    Flexible and tolerant, they take a pragmatic approach focused on immediate
    results. Theories and conceptual explanations bore them - they want to act
    energetically to solve the problem. Focus on the here- and-now,
    spontaneous, enjoy each moment that they can be active with others. Enjoy
    material comforts and style. Learn best through doing.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Esfp(MBTIType):
    """Determine the response for this type, given another type.

    Outgoing, friendly, and accepting. Exuberant lovers of life, people, and
    material comforts. Enjoy working with others to make things happen. Bring
    common sense and a realistic approach to their work, and make work fun.
    Flexible and spontaneous, adapt readily to new people and environments.
    Learn best by trying a new skill with other people.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Enfp(MBTIType):
    """Determine the response for this type, given another type.

    Warmly enthusiastic and imaginative. See life as full of possibilities.
    Make connections between events and information very quickly, and
    confidently proceed based on the patterns they see. Want a lot of
    affirmation from others, and readily give appreciation and support.
    Spontaneous and flexible, often rely on their ability to improvise and
    their verbal fluency.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Entp(MBTIType):
    """Determine the response for this type, given another type.

    Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving
    new and challenging problems. Adept at generating conceptual possibilities
    and then analyzing them strategically. Good at reading other people. Bored
    by routine, will seldom do the same thing the same way, apt to turn to one
    new interest after another.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Estj(MBTIType):
    """Determine the response for this type, given another type.

    Practical, realistic, matter-of-fact. Decisive, quickly move to implement
    decisions. Organize projects and people to get things done, focus on
    getting results In the most efficient way possible. Take care of routine
    details. Have a clear set of logical standards, systematically follow them
    and want others to also. Forceful in implementing their plans.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Esfj(MBTIType):
    """Determine the response for this type, given another type.

    Warmhearted, conscientious, and cooperative. Want harmony in their
    environment, work with determination to establish it. Like to work with
    others to complete tasks accurately and on time. Loyal, follow through even
    in small matters. Notice what others need in their day-by-day lives and try
    to provide it. Want to be appreciated for who they are and for what they
    contribute.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Enfj(MBTIType):
    """Determine the response for this type, given another type.

    Warm, empathetic, responsive, and responsible. Highly attuned to the
    emotions, needs, and motivations of others. Find potential in everyone,
    want to help others fulfill their potential. May act as catalysts for
    individual and group growth. Loyal, responsive to praise and criticism.
    Sociable, facilitate others in a group, and provide inspiring leadership.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


class Entj(MBTIType):
    """Determine the response for this type, given another type.

    Frank, decisive, assume leadership readily. Quickly see illogical and
    inefficient procedures and policies, develop and implement comprehensive
    systems to solve organizational problems. Enjoy long-term planning and goal
    setting. Usually well informed, well read, enjoy expanding their knowledge
    and passing it on to others. Forceful in presenting their ideas.
    """

    attrs = AttributeMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
