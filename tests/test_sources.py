import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('The Standard','KTN News#Get The Whole Story','Kenya facing two pandemics COVID-19 and floods cases with many deaths all over.','standardmedia.co.ke','general','Kenya','english')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'The Standard')
        self.assertEquals(self.new_source.name,'KTN News#Get The Whole Story')
        self.assertEquals(self.new_source.description,'Kenya facing two pandemics COVID-19 and floods cases with many deaths all over.')
        self.assertEqual(self.new_source.corona updates videoclip,'https://youtu.be/1sfsoLNcCn0')
        self.assertEqual(self.new_source.floods videoclip,'https://youtu.be/QzRiQ3r6tQs' )
        self.assertEquals(self.new_source.url,'standardmedia.co.ke')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'Kenya')
        self.assertEquals(self.new_source.language,'english')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('France24','JN','Protests continues in Minneapolis,Atlanta and Newyork.','Derek Chauvin charged with 3rd-degree and manslaughter in death of George Floyd,this has made many people to seek justice for the family by protesting.','lg.com','lg.com/lg.jpg','25-05-2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'France24')
        self.assertEquals(self.new_article.author,'JN')
        self.assertEquals(self.new_article.title,'Protest continues in Minneapolis,Atlanta and Newyork.')
        self.assertEquals(self.new_article.description,'Derek Chauvin charged with 3rd-degree and manslaughter in death of George Floyd,this has made many people to seek justice for the family by protesting.')
        self.assertEquals(self.new_article.videoclip,'https://youtu.be/iwPPqDryPO8')
        self.assertEquals(self.new_article.url,'JN.com')
        self.assertEquals(self.new_article.image,'JN.com/JN.jpg')
        self.assertEquals(self.new_article.date,'25-05-2020')
