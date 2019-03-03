# SisterHacks 2019 - Accessibility App
# Claudia Olson, Emma Kornberg, Hannah Yallof

#we should put in some type of back button so you don't need to close the function to get back to start

from graphics import *

def main():
    """ Sets up a window and draws objects on the screen
        Calls methods to open pages when buttons are clicked """
    win = GraphWin("Accessibility Website", 800, 600)
    win.setBackground("firebrick")
    title_btn = Button(Point(75, 25), Point(725, 100))
    title_btn.setFill("gold")
    title_btn.draw(win)
    title_btn_text = Text(Point(400, 62.5), "A Guide to Accessible Web Design")
    title_btn_text.setSize(36)
    title_btn_text.draw(win)

    rect = Rectangle(Point(50, 300), Point(750, 425))
    rect.setFill("dark orange")
    rect.draw(win)
    
    about_btn = Button(Point(200, 125), Point(600, 200))
    about_btn.setFill("gold")
    about_btn.draw(win)
    about_btn_text = Text(Point(400, 162.5), "About")
    about_btn_text.setSize(32)
    about_btn_text.draw(win)

    paragraph = Text(Point(350, 450),
"""Why is accessibility in web design important?

                        If you’ve ever ridden a skateboard or a bike or pushed a stroller on a sidewalk you’ve
                        directly benefited from accessible designs. You’ve experienced the Curb Cut effect. The
                        slopes that provide a smooth transition from roads to sidewalks, called curb cuts were
                        designed for people who are wheelchair bound, but everyone reaps the benefits from them.
                        
                        Web design works the same way. Many of the design choices made to assist the cognitively,
                        visually, and auditory impaired people also benefit anyone using your site in distracting
                        environments, people with low literacy or non-native speakers, people viewing the site on
                        mobile, or who are inexperienced with technology.

What does an accessible website look like?

                        That depends greatly on what issues you’re trying to be accessible for. On our main page,
                        we have guidelines and resources specifically for dyslexia, visual impairments like color
                        blindness and vision loss, and audio impairments. But there are some general good practices
                        that all sites should try to use.

Websites should have...
                        
                        *Both text and color indications for required sections to ensure they aren’t
                            missed by assistive technology or people with difficulty reading
                                    
                        *Every page should have a title with descriptive subsections
                                
                        *At least two lines of spacing before titles
                                
                        *Asterisks to indicate items in a list
                                
                        *Multiple ways to find relevant pages
                                
                        *Clearly-explained links""")
    
    audio_btn = AudioButton(Point(75, 325), Point(200, 400))
    audio_btn.setFill("gold")
    audio_btn.draw(win)
    audio_btn_text = Text(Point(137.5, 362.5), "Audio")
    audio_btn_text.setSize(32)
    audio_btn_text.draw(win)
    audio_paragraph = Text(Point(100,200), """ """)
    audio_sources_paragraph = Text(Point(350, 200), """
https://www.w3.org/standards/webdesign/accessibility#examples 
-(Transcripts)
https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#text-alternatives 
-(1.2.1-9 is all audio accessibility)
-(Transcripts, captions, or a detailed summary of any other information)
-(Sign language translation in the player is ideal)
https://www.w3.org/WAI/fundamentals/accessibility-principles/ 
-(User can pause, stop and adjust the volume of audio)
-(Background audio is low and can be turned off)
""")
    
    dyslexia_btn = DyslexiaButton(Point(337.5, 325), Point(462.5, 400))
    dyslexia_btn.setFill("gold")
    dyslexia_btn.draw(win)
    dyslexia_btn_text = Text(Point(400, 362.5), "Dyslexia")
    dyslexia_btn_text.setSize(32)
    dyslexia_btn_text.draw(win)
    dyslexia_paragraph = Text(Point(350,450),
                              """accessibility resources:

https://www.dyslexiefont.com/en/typeface/ 
- paid
- highly rated font
- different packages (word processor, pdf text converter, chrome extension, etc.)

https://www.opendyslexic.org/ 
- free
- second most highly rated font
- font download for use in word processing

http://www.beelinereader.com/ 
	- free and paid options
	- color gradient guide helps focus on and transition between lines
- good for reading paragraphs
	- different packages (browser/pdf plug-ins and ios/android apps)

ways to promote accessibility:

fonts
- sans serif typeface (eg. arial, comic sans)
- large font size (14-18pt)
- avoid italics when possible
- lower case letters

text blocks
- use headers and subheaders to break up text
- columns of text
- avoid wide spaced justification
- consistency is key

general
- no moving or changing text
- no time limits or interruptions
- low contrast between background and text

optimal color combinations:
1) black & yellow
2) blue & white
3) black & creme
4) black & white
5) blue & yellow
6) brown & dark green
7) off-black & off-white

when possible, allow for textual customization (colors, font size, typeface, etc.)
""")
    dyslexia_sources_paragraph = Text(Point(350, 250),"""
https://www.dyslexiefont.com/en/typeface/
-(example of a font, website has explanations about types of letters)
https://webaim.org/simulations/dyslexia
-(this is a simulator)
https://blog.changedyslexia.org/wp-content/uploads/2017/03/W4A2015-Synergies.pdf
-(guide by a Carnegie Mellon professor)
https://www.w3.org/WAI/fundamentals/accessibility-principles/ 
-(Avoid time limits, moving, blinking, or scrolling information, and interruptions)
-(Re-authenticate when the session expires without losing data)
https://link.springer.com/article/10.1007%2Fs10209-009-0160-5
-(Prioritize info)
-(No moving or changing text)
-(More organized/intuitive layout (clear headers, broken up information))
https://uxmovement.com/content/6-surprising-bad-practices-that-hurt-dyslexic-users/ 
-(No wide spaced justification)
""")
    
    visual_btn = VisualButton(Point(600, 325), Point(725, 400))
    visual_btn.setFill("gold")
    visual_btn.draw(win)
    visual_btn_text = Text(Point(662.5, 362.5), "Visual")
    visual_btn_text.setSize(32)
    visual_btn_text.draw(win)
    visual_paragraph = Text(Point(350,350),
"""Color Blindness:

3 Major Types
Deuteranopia - insensitivity to green
Protanopia - insensitivity to red
Tritanopia - insensitivity to blue

Ways to Promote Accessibility:
- Convey information with symbols other than color
- High Color Contrast
- Color palettes designed for color blindness

Vision Loss:

- Image captions
- Large font
- High contrast colors
- Use less graphics
- More distinct sections (vs large continuous blocks of text)
- Captions for images and diagrams
- Labels, detailed summaries, and transcripts for non-text items
- Decorative non-texts should not interfere with assistive technology
- Avoid images of text. If cannot be avoided,
    should be at least 200% enlargeable without losing information
""")

    click = True
    while click:
        mousePt = win.checkMouse()
        if mousePt is not None:
            if about_btn.getP1().getX() < mousePt.getX() < about_btn.getP2().getX():
                if about_btn.getP1().getY() < mousePt.getY() < about_btn.getP2().getY():
                    click = False
                    about_btn.onClick(win, "About", paragraph)
            if audio_btn.getP1().getX() < mousePt.getX() < audio_btn.getP2().getX():
                if audio_btn.getP1().getY() < mousePt.getY() < audio_btn.getP2().getY():
                    click = False
                    audio_btn.audioOnClick(win, "Audio", audio_paragraph, audio_sources_paragraph)
            if dyslexia_btn.getP1().getX() < mousePt.getX() < dyslexia_btn.getP2().getX():
                if dyslexia_btn.getP1().getY() < mousePt.getY() < dyslexia_btn.getP2().getY():
                    click = False
                    dyslexia_btn.dyslexiaOnClick(win, "Dyslexia", dyslexia_paragraph, dyslexia_sources_paragraph)
            if visual_btn.getP1().getX() < mousePt.getX() < visual_btn.getP2().getX():
                if visual_btn.getP1().getY() < mousePt.getY() < visual_btn.getP2().getY():
                    click = False
                    visual_btn.visualOnClick(win, "Visual", visual_paragraph)
        click = True
    
class Button(Rectangle):
    """ Button class: contains methods to construct
        a button and makes it interactive"""

    # creates a new window when the button is clicked
    def onClick(self, win, header, paragraph_text):
        win = GraphWin("Accessibility", 800, 800)
        win.setBackground("gold")
        header_text = Text(Point(100, 50), header)
        header_text.setSize(32)
        header_text.draw(win)
        paragraph_text.setSize(18)
        paragraph_text.draw(win)

class AudioButton(Button):

    def audioOnClick(self, audio_win, header, audio_paragraph, audio_sources_paragraph):
        audio_win = GraphWin("Audio", 800, 600)
        audio_win.setBackground("gold")
        header_text = Text(Point(100, 50), header)
        header_text.setSize(32)
        header_text.draw(audio_win)
        
        audio_info_btn = AudioInfoButton(Point(300, 100), Point(500, 200))
        audio_info_btn.setFill("light goldenrod yellow")
        audio_info_btn.draw(audio_win)
        audio_info_btn_text = Text(Point(400, 150), "Information")
        audio_info_btn_text.setSize(32)
        audio_info_btn_text.draw(audio_win)

        audio_sources_btn = AudioSourcesButton(Point(300, 300), Point(500, 400))
        audio_sources_btn.setFill("light goldenrod yellow")
        audio_sources_btn.draw(audio_win)
        audio_sources_btn_text = Text(Point(400, 350), "Sources")
        audio_sources_btn_text.setSize(32)
        audio_sources_btn_text.draw(audio_win)
        
        audio_click = True
        while audio_click:
            mousePt = audio_win.checkMouse()
            if mousePt is not None:
                if audio_info_btn.getP1().getX() < mousePt.getX() < audio_info_btn.getP2().getX():
                    if audio_info_btn.getP1().getY() < mousePt.getY() < audio_info_btn.getP2().getY():
                        audio_click = False
                        audio_info_btn.audioInfoOnClick(audio_win, "Audio Information", audio_paragraph)
                if audio_sources_btn.getP1().getX() < mousePt.getX() < audio_sources_btn.getP2().getX():
                    if audio_sources_btn.getP1().getY() < mousePt.getY() < audio_sources_btn.getP2().getY():
                        audio_click = False
                        audio_sources_btn.audioSourcesOnClick(audio_win, "Audio Sources", audio_sources_paragraph)

class AudioInfoButton(AudioButton):
    
    def audioInfoOnClick(self, audio_win, header, audio_paragraph):
        audio_info_win = GraphWin("Audio Information", 800, 600)
        audio_info_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(audio_info_win)
        audio_paragraph.setSize(18)
        audio_paragraph.draw(audio_info_win)
        
class AudioSourcesButton(AudioButton):
    
    def audioSourcesOnClick(self, audio_win, header, audio_sources_paragraph):
        audio_sources_win = GraphWin("Audio Sources", 800, 600)
        audio_sources_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(audio_sources_win)
        audio_sources_paragraph.setSize(18)
        audio_sources_paragraph.draw(audio_sources_win)

class DyslexiaButton(Button):

    def dyslexiaOnClick(self, dyslexia_win, header, dyslexia_paragraph, dyslexia_sources_paragraph):
        dyslexia_win = GraphWin("Dyslexia", 800, 600)
        dyslexia_win.setBackground("gold")
        header_text = Text(Point(100, 50), header)
        header_text.setSize(32)
        header_text.draw(dyslexia_win)
        
        dyslexia_info_btn = DyslexiaInfoButton(Point(300, 100), Point(500, 200))
        dyslexia_info_btn.setFill("light goldenrod yellow")
        dyslexia_info_btn.draw(dyslexia_win)
        dyslexia_info_btn_text = Text(Point(400, 150), "Information")
        dyslexia_info_btn_text.setSize(32)
        dyslexia_info_btn_text.draw(dyslexia_win)

        dyslexia_sources_btn = DyslexiaSourcesButton(Point(300, 300), Point(500, 400))
        dyslexia_sources_btn.setFill("light goldenrod yellow")
        dyslexia_sources_btn.draw(dyslexia_win)
        dyslexia_sources_btn_text = Text(Point(400, 350), "Sources")
        dyslexia_sources_btn_text.setSize(32)
        dyslexia_sources_btn_text.draw(dyslexia_win)
        
        dyslexia_click = True
        while dyslexia_click:
            mousePt = dyslexia_win.checkMouse()
            if mousePt is not None:
                if dyslexia_info_btn.getP1().getX() < mousePt.getX() < dyslexia_info_btn.getP2().getX():
                    if dyslexia_info_btn.getP1().getY() < mousePt.getY() < dyslexia_info_btn.getP2().getY():
                        dyslexia_click = False
                        dyslexia_info_btn.dyslexiaInfoOnClick(dyslexia_win, "Dyslexia Information", dyslexia_paragraph)
                    if dyslexia_sources_btn.getP1().getX() < mousePt.getX() < dyslexia_sources_btn.getP2().getX():
                        if dyslexia_sources_btn.getP1().getY() < mousePt.getY() < dyslexia_sources_btn.getP2().getY():
                            dyslexia_click = False
                            dyslexia_sources_btn.dyslexiaSourcesOnClick(dyslexia_win, "Dyslexia Sources", dyslexia_sources_paragraph)

class DyslexiaInfoButton(DyslexiaButton):
    
    def dyslexiaInfoOnClick(self, dyslexia_win, header, dyslexia_paragraph):
        dyslexia_info_win = GraphWin("Dyslexia Information", 800, 800)
        dyslexia_info_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(dyslexia_info_win)
        dyslexia_paragraph.setSize(12)
        dyslexia_paragraph.draw(dyslexia_info_win)
        
class DyslexiaSourcesButton(DyslexiaButton):
    
    def dyslexiaSourcesOnClick(self, dyslexia_win, header, dyslexia_sources_paragraph):
        dyslexia_sources_win = GraphWin("Dyslexia Sources", 800, 600)
        dyslexia_sources_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(dyslexia_sources_win)
        dyslexia_sources_paragraph.setSize(18)
        dyslexia_sources_paragraph.draw(dyslexia_sources_win)
        
class VisualButton(Button):

    def visualOnClick(self, visual_win, header, visual_paragraph):
        visual_win = GraphWin("Visual", 800, 600)
        visual_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(visual_win)

        visual_info_btn = VisualInfoButton(Point(300, 100), Point(500, 200))
        visual_info_btn.setFill("light goldenrod yellow")
        visual_info_btn.draw(visual_win)
        visual_info_btn_text = Text(Point(400, 150), "Information")
        visual_info_btn_text.setSize(32)
        visual_info_btn_text.draw(visual_win)

        visual_sources_btn = VisualSourcesButton(Point(300, 300), Point(500, 400))
        visual_sources_btn.setFill("light goldenrod yellow")
        visual_sources_btn.draw(visual_win)
        visual_sources_btn_text = Text(Point(400, 350), "Sources")
        visual_sources_btn_text.setSize(32)
        visual_sources_btn_text.draw(visual_win)
        
        visual_click = True
        while visual_click:
            mousePt = visual_win.checkMouse()
            if mousePt is not None:
                if visual_info_btn.getP1().getX() < mousePt.getX() < visual_info_btn.getP2().getX():
                    if visual_info_btn.getP1().getY() < mousePt.getY() < visual_info_btn.getP2().getY():
                        visual_click = False
                        visual_info_btn.visualInfoOnClick(visual_win, "Vision Information", visual_paragraph)
                    if visual_sources_btn.getP1().getX() < mousePt.getX() < visual_sources_btn.getP2().getX():
                        if visual_sources_btn.getP1().getY() < mousePt.getY() < visual_sources_btn.getP2().getY():
                            visual_click = False
                            visual_sources_btn.visualSourcesOnClick(visual_win, "Vision Sources")

class VisualInfoButton(VisualButton):
    
    def visualInfoOnClick(self, visual_win, header, visual_paragraph):
        visual_info_win = GraphWin("Visual Information", 800, 600)
        visual_info_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(visual_info_win)
        visual_paragraph.setSize(18)
        visual_paragraph.draw(visual_info_win)

class VisualSourcesButton(VisualButton):
    
    def visualSourcesOnClick(self, visual_win, header):
        visual_sources_win = GraphWin("Visual Sources", 800, 600)
        visual_sources_win.setBackground("gold")
        header_text = Text(Point(150, 50), header)
        header_text.setSize(32)
        header_text.draw(visual_sources_win)

if __name__ == "__main__":
    main()
