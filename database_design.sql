-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 27, 2020 at 03:52 PM
-- Server version: 5.7.29-cll-lve
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `metallic_1811_coursework`
--

-- --------------------------------------------------------

--
-- Table structure for table `gsuCandidateApplication`
--

CREATE TABLE `gsuCandidateApplication` (
  `applicationID` int(11) NOT NULL,
  `candidateID` int(11) NOT NULL,
  `positionID` int(11) NOT NULL,
  `electionID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `gsuCandidateApplication`
--

INSERT INTO `gsuCandidateApplication` (`applicationID`, `candidateID`, `positionID`, `electionID`) VALUES
(1, 19, 1, 1),
(2, 203, 1, 1),
(3, 52, 1, 1),
(4, 169, 1, 1),
(5, 44, 2, 1),
(6, 411, 2, 1),
(7, 84, 2, 1),
(8, 99, 2, 1),
(9, 413, 3, 1),
(10, 333, 3, 1),
(11, 1, 3, 1),
(12, 346, 3, 1),
(13, 415, 4, 1),
(14, 231, 4, 1),
(15, 371, 4, 1),
(16, 460, 4, 1),
(17, 312, 5, 1),
(18, 360, 5, 1),
(19, 25, 5, 1),
(20, 123, 5, 1),
(21, 251, 6, 1),
(22, 412, 6, 1),
(23, 144, 6, 1),
(24, 473, 6, 1),
(25, 338, 7, 1),
(26, 486, 7, 1),
(27, 143, 7, 1),
(28, 160, 7, 1),
(29, 386, 8, 1),
(30, 410, 8, 1),
(31, 402, 8, 1),
(32, 107, 8, 1),
(33, 450, 9, 1),
(34, 116, 9, 1),
(35, 487, 9, 1),
(36, 300, 9, 1),
(37, 481, 10, 1),
(38, 326, 10, 1),
(39, 195, 10, 1),
(40, 145, 10, 1),
(41, 8, 11, 1),
(42, 490, 11, 1),
(43, 151, 11, 1),
(44, 132, 11, 1),
(45, 26, 12, 1),
(46, 478, 12, 1),
(47, 269, 12, 1),
(48, 111, 12, 1),
(49, 373, 13, 1),
(50, 131, 13, 1),
(51, 103, 13, 1),
(52, 261, 13, 1),
(53, 262, 14, 1),
(54, 406, 14, 1),
(55, 147, 14, 1),
(56, 394, 14, 1),
(57, 405, 15, 1),
(58, 266, 15, 1),
(59, 137, 15, 1),
(60, 181, 15, 1),
(61, 158, 16, 1),
(62, 343, 16, 1),
(63, 139, 16, 1),
(64, 205, 16, 1),
(65, 444, 17, 1),
(66, 480, 17, 1),
(67, 494, 17, 1),
(68, 260, 17, 1),
(69, 271, 18, 1),
(70, 133, 18, 1),
(71, 458, 18, 1),
(72, 420, 18, 1),
(73, 9, 19, 1),
(74, 203, 19, 1),
(75, 495, 19, 1),
(76, 495, 19, 1);

-- --------------------------------------------------------

--
-- Table structure for table `gsuCandidates`
--

CREATE TABLE `gsuCandidates` (
  `candidateID` int(11) NOT NULL,
  `candidateName` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `candidateEmail` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `gsuCandidates`
--

INSERT INTO `gsuCandidates` (`candidateID`, `candidateName`, `candidateEmail`) VALUES
(1, 'Gertrudis Standfield', 'gstandfield0@walmart.com'),
(2, 'Zora Ayto', 'zayto1@yolasite.com'),
(3, 'Kiley Wanne', 'kwanne2@foxnews.com'),
(4, 'Elise Learie', 'elearie3@de.vu'),
(5, 'Jillayne Seabourne', 'jseabourne4@webs.com'),
(6, 'Lockwood Cutler', 'lcutler5@unc.edu'),
(7, 'Tiffi Truter', 'ttruter6@ask.com'),
(8, 'Madelin Strotton', 'mstrotton7@amazonaws.com'),
(9, 'Horacio Kelloch', 'hkelloch8@cbsnews.com'),
(10, 'Letitia Gerren', 'lgerren9@imdb.com'),
(11, 'Philippe Watkin', 'pwatkina@photobucket.com'),
(12, 'Petronella Sonner', 'psonnerb@house.gov'),
(13, 'Aldous Giffkins', 'agiffkinsc@cdc.gov'),
(14, 'Salim Crosetto', 'scrosettod@loc.gov'),
(15, 'Anny Cano', 'acanoe@skype.com'),
(16, 'Mair Bedle', 'mbedlef@mediafire.com'),
(17, 'Marti Kingsman', 'mkingsmang@vk.com'),
(18, 'Shaylynn Banaszczyk', 'sbanaszczykh@chicagotribune.com'),
(19, 'Hobie Stoodale', 'hstoodalei@com.com'),
(20, 'Lydon Jozsika', 'ljozsikaj@e-recht24.de'),
(21, 'Nisse Nower', 'nnowerk@constantcontact.com'),
(22, 'Wyndham Jowsey', 'wjowseyl@i2i.jp'),
(23, 'Pascale Inker', 'pinkerm@ehow.com'),
(24, 'Arnaldo Lougheed', 'alougheedn@businessinsider.com'),
(25, 'Vicky Cholwell', 'vcholwello@ihg.com'),
(26, 'Flore Copelli', 'fcopellip@howstuffworks.com'),
(27, 'Lindsay Ramiro', 'lramiroq@surveymonkey.com'),
(28, 'Magdalene Ollet', 'molletr@jiathis.com'),
(29, 'Gustav Renne', 'grennes@wufoo.com'),
(30, 'Claudio Vasyutkin', 'cvasyutkint@g.co'),
(31, 'Grier Fulham', 'gfulhamu@storify.com'),
(32, 'Kim Moylane', 'kmoylanev@dailymotion.com'),
(33, 'Eb Bruinemann', 'ebruinemannw@twitter.com'),
(34, 'Hal Lodge', 'hlodgex@nytimes.com'),
(35, 'Gearalt Clouston', 'gcloustony@unc.edu'),
(36, 'Norene Feechum', 'nfeechumz@oakley.com'),
(37, 'Delores Mottley', 'dmottley10@latimes.com'),
(38, 'Kacey Aujouanet', 'kaujouanet11@tmall.com'),
(39, 'Rhoda Fildery', 'rfildery12@wufoo.com'),
(40, 'Farr Marzelli', 'fmarzelli13@narod.ru'),
(41, 'Rozanne Gagan', 'rgagan14@wiley.com'),
(42, 'Harrietta Lamyman', 'hlamyman15@behance.net'),
(43, 'Ardath Boldra', 'aboldra16@earthlink.net'),
(44, 'Serena Yegorkin', 'syegorkin17@hud.gov'),
(45, 'Jakie Kamiyama', 'jkamiyama18@army.mil'),
(46, 'Daniela Thor', 'dthor19@abc.net.au'),
(47, 'Tomaso Sollime', 'tsollime1a@squarespace.com'),
(48, 'Andie Padillo', 'apadillo1b@com.com'),
(49, 'Codie Greenhaugh', 'cgreenhaugh1c@google.es'),
(50, 'Deborah Cabel', 'dcabel1d@exblog.jp'),
(51, 'Malinda Sails', 'msails1e@theguardian.com'),
(52, 'Emylee Escudier', 'eescudier1f@boston.com'),
(53, 'Sargent Vassie', 'svassie1g@webeden.co.uk'),
(54, 'Wally Dochon', 'wdochon1h@livejournal.com'),
(55, 'Berti Garmon', 'bgarmon1i@zimbio.com'),
(56, 'Mirilla Sinncock', 'msinncock1j@elegantthemes.com'),
(57, 'Amabelle Ortega', 'aortega1k@delicious.com'),
(58, 'Matthus Mapplethorpe', 'mmapplethorpe1l@unblog.fr'),
(59, 'Olivia Ambrozewicz', 'oambrozewicz1m@studiopress.com'),
(60, 'Inger Roderigo', 'iroderigo1n@plala.or.jp'),
(61, 'Georgetta Redgate', 'gredgate1o@usatoday.com'),
(62, 'Marietta Lincoln', 'mlincoln1p@ameblo.jp'),
(63, 'Tom Whitemarsh', 'twhitemarsh1q@eventbrite.com'),
(64, 'Lindsay Addams', 'laddams1r@msu.edu'),
(65, 'Langsdon Wakelam', 'lwakelam1s@over-blog.com'),
(66, 'Merna Gregine', 'mgregine1t@yellowpages.com'),
(67, 'Antoinette Geraud', 'ageraud1u@cornell.edu'),
(68, 'Gal Helsdon', 'ghelsdon1v@npr.org'),
(69, 'Danette Bethune', 'dbethune1w@vistaprint.com'),
(70, 'Christos Wethered', 'cwethered1x@g.co'),
(71, 'Dorthy Marfe', 'dmarfe1y@skyrock.com'),
(72, 'Ralf Brignall', 'rbrignall1z@abc.net.au'),
(73, 'Rora Prawle', 'rprawle20@geocities.com'),
(74, 'Russ Everett', 'reverett21@simplemachines.org'),
(75, 'Quill Vallow', 'qvallow22@bing.com'),
(76, 'Hodge Flay', 'hflay23@disqus.com'),
(77, 'Gail Odo', 'godo24@issuu.com'),
(78, 'Keefer Faveryear', 'kfaveryear25@columbia.edu'),
(79, 'Amii Scantleberry', 'ascantleberry26@wsj.com'),
(80, 'Arlena Rosetti', 'arosetti27@vinaora.com'),
(81, 'Dorice Chern', 'dchern28@deliciousdays.com'),
(82, 'Bettina Heintze', 'bheintze29@yandex.ru'),
(83, 'Clive Billes', 'cbilles2a@cam.ac.uk'),
(84, 'Annnora Klimuk', 'aklimuk2b@google.co.jp'),
(85, 'Breena Janodet', 'bjanodet2c@eventbrite.com'),
(86, 'Beale Wragge', 'bwragge2d@360.cn'),
(87, 'Giana Kilshaw', 'gkilshaw2e@tuttocitta.it'),
(88, 'Winifield Clifton', 'wclifton2f@hao123.com'),
(89, 'Agace Offner', 'aoffner2g@flickr.com'),
(90, 'Shalom Pritchett', 'spritchett2h@yellowpages.com'),
(91, 'Butch Whether', 'bwhether2i@clickbank.net'),
(92, 'Kamila Laurenceau', 'klaurenceau2j@opera.com'),
(93, 'Tove Tryme', 'ttryme2k@pinterest.com'),
(94, 'Rockey Baiyle', 'rbaiyle2l@foxnews.com'),
(95, 'Willis Bone', 'wbone2m@squarespace.com'),
(96, 'Terra Devanny', 'tdevanny2n@trellian.com'),
(97, 'Heather Ullett', 'hullett2o@huffingtonpost.com'),
(98, 'Ania Glozman', 'aglozman2p@ca.gov'),
(99, 'Hadleigh Fassan', 'hfassan2q@vistaprint.com'),
(100, 'Malachi Cowgill', 'mcowgill2r@tinyurl.com'),
(101, 'Tammy Meletti', 'tmeletti2s@goo.ne.jp'),
(102, 'Willy Egdal', 'wegdal2t@nymag.com'),
(103, 'Maximilian Dalrymple', 'mdalrymple2u@merriam-webster.com'),
(104, 'Dylan Depke', 'ddepke2v@behance.net'),
(105, 'Cecil Oran', 'coran2w@1688.com'),
(106, 'Tully Spawton', 'tspawton2x@gizmodo.com'),
(107, 'Huberto Martijn', 'hmartijn2y@pbs.org'),
(108, 'Coleman Coneley', 'cconeley2z@wikia.com'),
(109, 'Kaye Fisher', 'kfisher30@360.cn'),
(110, 'Levey Pevreal', 'lpevreal31@parallels.com'),
(111, 'Leodora Have', 'lhave32@boston.com'),
(112, 'Cos Fursey', 'cfursey33@yolasite.com'),
(113, 'Nikkie Pellew', 'npellew34@jimdo.com'),
(114, 'Torrie Ledster', 'tledster35@exblog.jp'),
(115, 'Dannel Anfrey', 'danfrey36@prweb.com'),
(116, 'Hanna Cristea', 'hcristea37@oaic.gov.au'),
(117, 'Lawton Acum', 'lacum38@umn.edu'),
(118, 'Aylmar Salomon', 'asalomon39@epa.gov'),
(119, 'Morty Tithacott', 'mtithacott3a@vinaora.com'),
(120, 'Skip Gothard', 'sgothard3b@kickstarter.com'),
(121, 'Matthieu Amberson', 'mamberson3c@dailymail.co.uk'),
(122, 'Eduard Duffrie', 'eduffrie3d@i2i.jp'),
(123, 'Del Brunotti', 'dbrunotti3e@nytimes.com'),
(124, 'Clo Bunford', 'cbunford3f@uol.com.br'),
(125, 'Dotty Edess', 'dedess3g@yolasite.com'),
(126, 'Reginald McCluin', 'rmccluin3h@biglobe.ne.jp'),
(127, 'Adela Zecchi', 'azecchi3i@w3.org'),
(128, 'Dillon Ledbetter', 'dledbetter3j@washington.edu'),
(129, 'Jacqueline Humpage', 'jhumpage3k@slate.com'),
(130, 'Brock Flew', 'bflew3l@nba.com'),
(131, 'Candida Domingues', 'cdomingues3m@booking.com'),
(132, 'Drona Stuehmeyer', 'dstuehmeyer3n@nymag.com'),
(133, 'Sheilah Pattisson', 'spattisson3o@chronoengine.com'),
(134, 'Dredi Stenson', 'dstenson3p@clickbank.net'),
(135, 'Marylynne Bennell', 'mbennell3q@slate.com'),
(136, 'Kyle Ales', 'kales3r@amazonaws.com'),
(137, 'Concordia Stit', 'cstit3s@360.cn'),
(138, 'Irving Ranns', 'iranns3t@alibaba.com'),
(139, 'Oona Ipsgrave', 'oipsgrave3u@usgs.gov'),
(140, 'Patty Ashtonhurst', 'pashtonhurst3v@samsung.com'),
(141, 'Ernestine Arden', 'earden3w@cnet.com'),
(142, 'Cobbie Berthomier', 'cberthomier3x@sun.com'),
(143, 'Bartolomeo Bernardeschi', 'bbernardeschi3y@g.co'),
(144, 'Patton Larver', 'plarver3z@sciencedaily.com'),
(145, 'Timotheus Liddiard', 'tliddiard40@blinklist.com'),
(146, 'Junina Sedge', 'jsedge41@dell.com'),
(147, 'Rozanna Argente', 'rargente42@comcast.net'),
(148, 'Ira Gwilt', 'igwilt43@ft.com'),
(149, 'Jandy Kingscote', 'jkingscote44@imdb.com'),
(150, 'Rae Keen', 'rkeen45@purevolume.com'),
(151, 'Errick Brave', 'ebrave46@latimes.com'),
(152, 'Fernanda Riach', 'friach47@spiegel.de'),
(153, 'Adorne Death', 'adeath48@sakura.ne.jp'),
(154, 'Aime Jiggle', 'ajiggle49@nydailynews.com'),
(155, 'Lanny Nerger', 'lnerger4a@ucoz.com'),
(156, 'Lani Hotchkin', 'lhotchkin4b@berkeley.edu'),
(157, 'Brooks Rubke', 'brubke4c@examiner.com'),
(158, 'Fabien O\' Donohoe', 'fo4d@altervista.org'),
(159, 'Erica Pykerman', 'epykerman4e@istockphoto.com'),
(160, 'Ollie Brand-Hardy', 'obrandhardy4f@altervista.org'),
(161, 'Alyosha Ellerby', 'aellerby4g@oakley.com'),
(162, 'Tami Miliffe', 'tmiliffe4h@amazon.co.uk'),
(163, 'Amabel Scrancher', 'ascrancher4i@ow.ly'),
(164, 'Paule Heatley', 'pheatley4j@home.pl'),
(165, 'Chuck Brownsill', 'cbrownsill4k@google.com.hk'),
(166, 'Shae Smissen', 'ssmissen4l@a8.net'),
(167, 'Paxton Gingell', 'pgingell4m@bravesites.com'),
(168, 'Biron Kundert', 'bkundert4n@zimbio.com'),
(169, 'Kimble Hunday', 'khunday4o@yellowpages.com'),
(170, 'Emlynne Prandy', 'eprandy4p@ehow.com'),
(171, 'Lydon Dunkley', 'ldunkley4q@google.ca'),
(172, 'Shaylynn Oxenden', 'soxenden4r@cpanel.net'),
(173, 'Nicolai Bigby', 'nbigby4s@360.cn'),
(174, 'Si Peegrem', 'speegrem4t@cpanel.net'),
(175, 'Tiler Wallbanks', 'twallbanks4u@sciencedaily.com'),
(176, 'Clemente Guitte', 'cguitte4v@marriott.com'),
(177, 'Lance Fieldsend', 'lfieldsend4w@prlog.org'),
(178, 'Cross Chasteney', 'cchasteney4x@istockphoto.com'),
(179, 'June Mc Queen', 'jmc4y@com.com'),
(180, 'Jere Pasquale', 'jpasquale4z@amazon.co.uk'),
(181, 'Jorgan Jecks', 'jjecks50@soundcloud.com'),
(182, 'Crawford Stockney', 'cstockney51@sphinn.com'),
(183, 'Kaitlynn Hedge', 'khedge52@nih.gov'),
(184, 'Avery Spaice', 'aspaice53@tuttocitta.it'),
(185, 'Joelle Fanti', 'jfanti54@netscape.com'),
(186, 'Brande Merfin', 'bmerfin55@t.co'),
(187, 'Louie Hayzer', 'lhayzer56@free.fr'),
(188, 'Trix Baruch', 'tbaruch57@dailymail.co.uk'),
(189, 'Camala Biffin', 'cbiffin58@google.es'),
(190, 'Jazmin Hedden', 'jhedden59@cocolog-nifty.com'),
(191, 'Rosemarie Campanelli', 'rcampanelli5a@tmall.com'),
(192, 'Kent Howat', 'khowat5b@wunderground.com'),
(193, 'Marley Vasichev', 'mvasichev5c@google.cn'),
(194, 'Nert Huntriss', 'nhuntriss5d@netvibes.com'),
(195, 'Alberik Basek', 'abasek5e@blinklist.com'),
(196, 'Elijah Timperley', 'etimperley5f@baidu.com'),
(197, 'Had Parsley', 'hparsley5g@seesaa.net'),
(198, 'Nikolia Hinrichs', 'nhinrichs5h@studiopress.com'),
(199, 'Archy Spreadbury', 'aspreadbury5i@shop-pro.jp'),
(200, 'Jamaal Tolan', 'jtolan5j@sourceforge.net'),
(201, 'Bettye Lamcken', 'blamcken5k@lulu.com'),
(202, 'Ivy L\'argent', 'ilargent5l@kickstarter.com'),
(203, 'Aurilia Bratchell', 'abratchell5m@yellowpages.com'),
(204, 'Kaela O\' Faherty', 'ko5n@youku.com'),
(205, 'Kasey Quiney', 'kquiney5o@uol.com.br'),
(206, 'Goldy Jeskin', 'gjeskin5p@qq.com'),
(207, 'Trumann Caves', 'tcaves5q@yale.edu'),
(208, 'Marjory Clink', 'mclink5r@nyu.edu'),
(209, 'Holmes O\' Donohoe', 'ho5s@over-blog.com'),
(210, 'Pablo Shevill', 'pshevill5t@nature.com'),
(211, 'Hurley Mowne', 'hmowne5u@imageshack.us'),
(212, 'Lenka Elmhurst', 'lelmhurst5v@domainmarket.com'),
(213, 'Vincent Phillot', 'vphillot5w@alibaba.com'),
(214, 'Wynn Bricket', 'wbricket5x@canalblog.com'),
(215, 'Udell Balden', 'ubalden5y@opera.com'),
(216, 'Filbert Ilyin', 'filyin5z@gnu.org'),
(217, 'Gaston Thynne', 'gthynne60@networkadvertising.org'),
(218, 'Anni Osmar', 'aosmar61@wufoo.com'),
(219, 'Brittany Clementet', 'bclementet62@google.com.hk'),
(220, 'Jemima Dennehy', 'jdennehy63@yandex.ru'),
(221, 'Maritsa Antrag', 'mantrag64@telegraph.co.uk'),
(222, 'Kellyann Loges', 'kloges65@rakuten.co.jp'),
(223, 'Elysia Bellino', 'ebellino66@flickr.com'),
(224, 'Aurilia Overington', 'aoverington67@imdb.com'),
(225, 'Padriac Othen', 'pothen68@deliciousdays.com'),
(226, 'Zea Whetnall', 'zwhetnall69@spiegel.de'),
(227, 'Prudy Bartolic', 'pbartolic6a@cdc.gov'),
(228, 'Nahum Doran', 'ndoran6b@java.com'),
(229, 'Winnah Piotrowski', 'wpiotrowski6c@rediff.com'),
(230, 'Josselyn Rubi', 'jrubi6d@bizjournals.com'),
(231, 'Ianthe Fergusson', 'ifergusson6e@t.co'),
(232, 'Saunders Dinnage', 'sdinnage6f@theglobeandmail.com'),
(233, 'Sybil McIlvenny', 'smcilvenny6g@ebay.co.uk'),
(234, 'Ber Gamlin', 'bgamlin6h@java.com'),
(235, 'Simeon Duker', 'sduker6i@dmoz.org'),
(236, 'Carmela Woolland', 'cwoolland6j@wikispaces.com'),
(237, 'Mayer Waby', 'mwaby6k@nifty.com'),
(238, 'Bride Vicarey', 'bvicarey6l@edublogs.org'),
(239, 'Abbey Lynnitt', 'alynnitt6m@google.pl'),
(240, 'Zandra Piscot', 'zpiscot6n@telegraph.co.uk'),
(241, 'Berty Erley', 'berley6o@goo.gl'),
(242, 'Corny Shalliker', 'cshalliker6p@goodreads.com'),
(243, 'Marcelle Tourville', 'mtourville6q@time.com'),
(244, 'Collin Gepp', 'cgepp6r@google.co.jp'),
(245, 'Burlie Crevagh', 'bcrevagh6s@cocolog-nifty.com'),
(246, 'Elvyn Pane', 'epane6t@techcrunch.com'),
(247, 'Sibby Wilfing', 'swilfing6u@netscape.com'),
(248, 'Kasey Grebert', 'kgrebert6v@exblog.jp'),
(249, 'Ulrikaumeko Lownsbrough', 'ulownsbrough6w@behance.net'),
(250, 'Bradney Gallagher', 'bgallagher6x@shop-pro.jp'),
(251, 'Sari Blinco', 'sblinco6y@jigsy.com'),
(252, 'Marti Bartosiak', 'mbartosiak6z@nytimes.com'),
(253, 'Trisha Cottel', 'tcottel70@samsung.com'),
(254, 'Michal Hawley', 'mhawley71@guardian.co.uk'),
(255, 'Bettye Betz', 'bbetz72@yahoo.com'),
(256, 'Gillie Matterdace', 'gmatterdace73@pbs.org'),
(257, 'Dallis Oram', 'doram74@issuu.com'),
(258, 'Kenyon Dwire', 'kdwire75@slashdot.org'),
(259, 'Winn Greer', 'wgreer76@stanford.edu'),
(260, 'Norrie Gyppes', 'ngyppes77@nationalgeographic.com'),
(261, 'Vassily Bick', 'vbick78@psu.edu'),
(262, 'Ida Mcwhinney', 'imcwhinney79@discuz.net'),
(263, 'Garreth D\'eath', 'gdeath7a@youtu.be'),
(264, 'Toby Ramas', 'tramas7b@accuweather.com'),
(265, 'Borg Bover', 'bbover7c@marriott.com'),
(266, 'Davine Sange', 'dsange7d@marriott.com'),
(267, 'Gram Spirit', 'gspirit7e@rambler.ru'),
(268, 'Calli Newbury', 'cnewbury7f@alexa.com'),
(269, 'Margo Jerman', 'mjerman7g@addtoany.com'),
(270, 'Joanne Duley', 'jduley7h@aol.com'),
(271, 'Mateo Wildblood', 'mwildblood7i@omniture.com'),
(272, 'Anna Tamburo', 'atamburo7j@freewebs.com'),
(273, 'Jami Sivewright', 'jsivewright7k@ft.com'),
(274, 'Eugenie Tolerton', 'etolerton7l@buzzfeed.com'),
(275, 'Kirby Abate', 'kabate7m@ft.com'),
(276, 'Octavia Blacklidge', 'oblacklidge7n@bloglines.com'),
(277, 'Devin Mompesson', 'dmompesson7o@so-net.ne.jp'),
(278, 'Camey Fusco', 'cfusco7p@noaa.gov'),
(279, 'Chrystel Avraham', 'cavraham7q@clickbank.net'),
(280, 'Druci De Cruze', 'dde7r@friendfeed.com'),
(281, 'Joletta Wallentin', 'jwallentin7s@amazonaws.com'),
(282, 'Miltie Radke', 'mradke7t@weather.com'),
(283, 'Lewes Charlwood', 'lcharlwood7u@wix.com'),
(284, 'Burlie Reeders', 'breeders7v@4shared.com'),
(285, 'Janna Tanton', 'jtanton7w@state.gov'),
(286, 'Celestyna Haswall', 'chaswall7x@bluehost.com'),
(287, 'Karrie Stathers', 'kstathers7y@slate.com'),
(288, 'Bert Brute', 'bbrute7z@cam.ac.uk'),
(289, 'Marten Seaborne', 'mseaborne80@github.com'),
(290, 'Dulsea Leopard', 'dleopard81@indiatimes.com'),
(291, 'Ingar McKmurrie', 'imckmurrie82@businessweek.com'),
(292, 'Teirtza Gayther', 'tgayther83@tinyurl.com'),
(293, 'Shelli McCreadie', 'smccreadie84@nationalgeographic.com'),
(294, 'Audrye Gare', 'agare85@nps.gov'),
(295, 'Theodor Garling', 'tgarling86@google.de'),
(296, 'Herminia Caston', 'hcaston87@storify.com'),
(297, 'Marisa Huckett', 'mhuckett88@virginia.edu'),
(298, 'Farleigh Flaverty', 'fflaverty89@jimdo.com'),
(299, 'Audry Acory', 'aacory8a@behance.net'),
(300, 'Carilyn McKinstry', 'cmckinstry8b@hhs.gov'),
(301, 'Phillipp Cullagh', 'pcullagh8c@flickr.com'),
(302, 'Marty Tuffley', 'mtuffley8d@wordpress.com'),
(303, 'Clary Nozzolinii', 'cnozzolinii8e@dell.com'),
(304, 'Cristin D\'Enrico', 'cdenrico8f@berkeley.edu'),
(305, 'Ernestus Clayworth', 'eclayworth8g@adobe.com'),
(306, 'Cary Bartlomiej', 'cbartlomiej8h@fastcompany.com'),
(307, 'Nonah Causbey', 'ncausbey8i@is.gd'),
(308, 'Ario Gostling', 'agostling8j@godaddy.com'),
(309, 'Romola Carding', 'rcarding8k@sogou.com'),
(310, 'Sheffield Osbaldstone', 'sosbaldstone8l@theglobeandmail.com'),
(311, 'Orsa Hardwick', 'ohardwick8m@cpanel.net'),
(312, 'Patty Depka', 'pdepka8n@arizona.edu'),
(313, 'Rahal Lazenby', 'rlazenby8o@addthis.com'),
(314, 'Kristine Yeliashev', 'kyeliashev8p@de.vu'),
(315, 'Shawn Schrader', 'sschrader8q@github.io'),
(316, 'Jannelle Wolsey', 'jwolsey8r@wix.com'),
(317, 'Maxi Adrian', 'madrian8s@tmall.com'),
(318, 'Saleem Tabourel', 'stabourel8t@illinois.edu'),
(319, 'Matt Cone', 'mcone8u@hostgator.com'),
(320, 'Byron Alp', 'balp8v@disqus.com'),
(321, 'Eddy Redemile', 'eredemile8w@homestead.com'),
(322, 'Ajay Doudny', 'adoudny8x@marriott.com'),
(323, 'Violante Snazle', 'vsnazle8y@liveinternet.ru'),
(324, 'Nance Charrisson', 'ncharrisson8z@sina.com.cn'),
(325, 'Pegeen Maxwale', 'pmaxwale90@exblog.jp'),
(326, 'Bealle Peppard', 'bpeppard91@independent.co.uk'),
(327, 'Wilhelmina Clempton', 'wclempton92@answers.com'),
(328, 'Wendall Gamlin', 'wgamlin93@taobao.com'),
(329, 'Mar Victor', 'mvictor94@kickstarter.com'),
(330, 'Morley McConnal', 'mmcconnal95@jigsy.com'),
(331, 'Kayla Pomfrett', 'kpomfrett96@vistaprint.com'),
(332, 'Wolf Kaasman', 'wkaasman97@newsvine.com'),
(333, 'Khalil Clatworthy', 'kclatworthy98@prweb.com'),
(334, 'Jacques Lande', 'jlande99@hhs.gov'),
(335, 'Peter Bridal', 'pbridal9a@bbc.co.uk'),
(336, 'Mariele McKie', 'mmckie9b@cafepress.com'),
(337, 'Gerik Upshall', 'gupshall9c@seattletimes.com'),
(338, 'Felicity Annice', 'fannice9d@amazonaws.com'),
(339, 'Gerri Duiged', 'gduiged9e@istockphoto.com'),
(340, 'Elissa Peagrim', 'epeagrim9f@wikipedia.org'),
(341, 'Deirdre Vawton', 'dvawton9g@nba.com'),
(342, 'Stanwood Koenen', 'skoenen9h@harvard.edu'),
(343, 'Thebault Rentelll', 'trentelll9i@economist.com'),
(344, 'Bella Millsom', 'bmillsom9j@constantcontact.com'),
(345, 'Morse Oehme', 'moehme9k@marriott.com'),
(346, 'Lelia Manion', 'lmanion9l@altervista.org'),
(347, 'Welby Hayzer', 'whayzer9m@lulu.com'),
(348, 'Zacharia Claessens', 'zclaessens9n@shutterfly.com'),
(349, 'Izak Roback', 'iroback9o@aol.com'),
(350, 'Chaim Fleeman', 'cfleeman9p@weebly.com'),
(351, 'Meris Ranstead', 'mranstead9q@zimbio.com'),
(352, 'Caddric Facey', 'cfacey9r@xrea.com'),
(353, 'Clarence Hanna', 'channa9s@cpanel.net'),
(354, 'Boony Petruszka', 'bpetruszka9t@indiegogo.com'),
(355, 'Edlin Ellson', 'eellson9u@stanford.edu'),
(356, 'Winny Seegar', 'wseegar9v@mashable.com'),
(357, 'Con Blything', 'cblything9w@illinois.edu'),
(358, 'Violette Kollasch', 'vkollasch9x@parallels.com'),
(359, 'Dodie Sorbie', 'dsorbie9y@hc360.com'),
(360, 'Dimitry Klimas', 'dklimas9z@fc2.com'),
(361, 'Konstance Matisoff', 'kmatisoffa0@linkedin.com'),
(362, 'Aldridge Byforth', 'abyfortha1@yandex.ru'),
(363, 'Tiffanie Tuerena', 'ttuerenaa2@imgur.com'),
(364, 'Carolus Milillo', 'cmililloa3@whitehouse.gov'),
(365, 'Heddi Harnor', 'hharnora4@bigcartel.com'),
(366, 'Valentia Manton', 'vmantona5@mapy.cz'),
(367, 'Marcel Micheu', 'mmicheua6@nationalgeographic.com'),
(368, 'Brittany Barbie', 'bbarbiea7@ibm.com'),
(369, 'Norene Tiuit', 'ntiuita8@liveinternet.ru'),
(370, 'Darrell Mullenger', 'dmullengera9@shareasale.com'),
(371, 'Stephi Quernel', 'squernelaa@ustream.tv'),
(372, 'Ardella Botha', 'abothaab@behance.net'),
(373, 'Lionel Rosenstiel', 'lrosenstielac@yale.edu'),
(374, 'Kevon Mulkerrins', 'kmulkerrinsad@hao123.com'),
(375, 'Thomasine Fernley', 'tfernleyae@printfriendly.com'),
(376, 'Dom Esslemont', 'desslemontaf@wikimedia.org'),
(377, 'Else Haughian', 'ehaughianag@tinypic.com'),
(378, 'Tommi Sked', 'tskedah@addthis.com'),
(379, 'Dalenna Hankey', 'dhankeyai@youtu.be'),
(380, 'Jessee Buzek', 'jbuzekaj@webmd.com'),
(381, 'Cesya Fawdery', 'cfawderyak@example.com'),
(382, 'Griffie Blaza', 'gblazaal@pcworld.com'),
(383, 'Belva Woofinden', 'bwoofindenam@rakuten.co.jp'),
(384, 'Roxanna Killelea', 'rkilleleaan@blinklist.com'),
(385, 'Inga Vango', 'ivangoao@clickbank.net'),
(386, 'Brandon Darrigone', 'bdarrigoneap@blog.com'),
(387, 'Chrisy Kaysor', 'ckaysoraq@g.co'),
(388, 'Norina Vernazza', 'nvernazzaar@networksolutions.com'),
(389, 'Juliana O\'Dunneen', 'jodunneenas@typepad.com'),
(390, 'Brennan Corrison', 'bcorrisonat@hud.gov'),
(391, 'Darwin Brotherhead', 'dbrotherheadau@wix.com'),
(392, 'Coretta Cleaton', 'ccleatonav@rambler.ru'),
(393, 'Reuven Body', 'rbodyaw@slashdot.org'),
(394, 'Gussy Grundon', 'ggrundonax@dmoz.org'),
(395, 'Genevieve Deeson', 'gdeesonay@sourceforge.net'),
(396, 'Alexa Janauschek', 'ajanauschekaz@parallels.com'),
(397, 'Alina Broughton', 'abroughtonb0@drupal.org'),
(398, 'Lindsay Langhor', 'llanghorb1@cornell.edu'),
(399, 'Brody Toth', 'btothb2@redcross.org'),
(400, 'Eimile Duffell', 'eduffellb3@netlog.com'),
(401, 'Alleen Soitoux', 'asoitouxb4@vinaora.com'),
(402, 'Wildon Boddice', 'wboddiceb5@time.com'),
(403, 'Royall Bowton', 'rbowtonb6@1und1.de'),
(404, 'Bettina Josofovitz', 'bjosofovitzb7@diigo.com'),
(405, 'Erl Riquet', 'eriquetb8@dot.gov'),
(406, 'Sherill Rummery', 'srummeryb9@live.com'),
(407, 'Christophorus Ecles', 'ceclesba@sina.com.cn'),
(408, 'Ky Robberecht', 'krobberechtbb@reverbnation.com'),
(409, 'Richmond Howbrook', 'rhowbrookbc@ucoz.com'),
(410, 'Melany Forrest', 'mforrestbd@illinois.edu'),
(411, 'Caitlin Keelan', 'ckeelanbe@github.io'),
(412, 'Jessie Tembey', 'jtembeybf@pinterest.com'),
(413, 'Lambert Yepiskopov', 'lyepiskopovbg@nifty.com'),
(414, 'Lorena Livesley', 'llivesleybh@economist.com'),
(415, 'Yovonnda Waring', 'ywaringbi@mapquest.com'),
(416, 'Kellsie Tregonna', 'ktregonnabj@marriott.com'),
(417, 'Stan Faherty', 'sfahertybk@ehow.com'),
(418, 'Halley Gerlts', 'hgerltsbl@patch.com'),
(419, 'Halley Vinter', 'hvinterbm@globo.com'),
(420, 'Germain Fishleigh', 'gfishleighbn@gizmodo.com'),
(421, 'Esmeralda Izakovitz', 'eizakovitzbo@de.vu'),
(422, 'Cobbie Braganca', 'cbragancabp@fc2.com'),
(423, 'Jimmie McGougan', 'jmcgouganbq@samsung.com'),
(424, 'Rickey Clardge', 'rclardgebr@icio.us'),
(425, 'Vicki Chong', 'vchongbs@loc.gov'),
(426, 'Chance Frenchum', 'cfrenchumbt@comsenz.com'),
(427, 'Malvina Pensom', 'mpensombu@sohu.com'),
(428, 'Kevon McReidy', 'kmcreidybv@jimdo.com'),
(429, 'Justino Carlino', 'jcarlinobw@youtube.com'),
(430, 'Sawyere Rigeby', 'srigebybx@zimbio.com'),
(431, 'Collete Bierling', 'cbierlingby@harvard.edu'),
(432, 'Myrle Skakunas', 'mskakunasbz@tumblr.com'),
(433, 'Korey Featherstonehaugh', 'kfeatherstonehaughc0@parallels.com'),
(434, 'Vyky Hellier', 'vhellierc1@accuweather.com'),
(435, 'Jesse Ivanchov', 'jivanchovc2@nifty.com'),
(436, 'Daryle Antao', 'dantaoc3@skyrock.com'),
(437, 'Caria Howe', 'chowec4@yale.edu'),
(438, 'Stavros Bachelor', 'sbachelorc5@posterous.com'),
(439, 'Freeman Eagle', 'feaglec6@wordpress.org'),
(440, 'Hadria Sains', 'hsainsc7@reuters.com'),
(441, 'Fletcher Buckney', 'fbuckneyc8@yellowbook.com'),
(442, 'Eduard Tivers', 'etiversc9@netvibes.com'),
(443, 'Judy Prangley', 'jprangleyca@zdnet.com'),
(444, 'Eba Berresford', 'eberresfordcb@mayoclinic.com'),
(445, 'Bernie Spolton', 'bspoltoncc@va.gov'),
(446, 'Gwyneth Perillio', 'gperilliocd@ning.com'),
(447, 'Jackquelin Stepney', 'jstepneyce@disqus.com'),
(448, 'Ber Corder', 'bcordercf@businessweek.com'),
(449, 'Orson Witherop', 'owitheropcg@dmoz.org'),
(450, 'Ole Swepstone', 'oswepstonech@stanford.edu'),
(451, 'Vidovic McLenaghan', 'vmclenaghanci@who.int'),
(452, 'Anallise Loudian', 'aloudiancj@hud.gov'),
(453, 'Anissa Infantino', 'ainfantinock@ifeng.com'),
(454, 'Coraline Maplethorp', 'cmaplethorpcl@comsenz.com'),
(455, 'Janeva Fores', 'jforescm@about.me'),
(456, 'Mame Bonnor', 'mbonnorcn@goo.gl'),
(457, 'Julia Larrat', 'jlarratco@nih.gov'),
(458, 'Zachery Beachamp', 'zbeachampcp@cam.ac.uk'),
(459, 'Harlie Harmant', 'hharmantcq@comcast.net'),
(460, 'Eimile Diperaus', 'ediperauscr@forbes.com'),
(461, 'Cynthy Middle', 'cmiddlecs@clickbank.net'),
(462, 'Deena Ownsworth', 'downsworthct@creativecommons.org'),
(463, 'Rahel Sawkin', 'rsawkincu@t.co'),
(464, 'Lotty Unworth', 'lunworthcv@ed.gov'),
(465, 'Adaline Wathan', 'awathancw@ask.com'),
(466, 'Malcolm Fend', 'mfendcx@time.com'),
(467, 'Olia Pirie', 'opiriecy@blog.com'),
(468, 'Frankie Fairburne', 'ffairburnecz@fc2.com'),
(469, 'Isabelita Biddwell', 'ibiddwelld0@mozilla.org'),
(470, 'Vanya Timpany', 'vtimpanyd1@cafepress.com'),
(471, 'Demeter Northridge', 'dnorthridged2@nhs.uk'),
(472, 'Dov Gotcliffe', 'dgotcliffed3@technorati.com'),
(473, 'Parker Klassman', 'pklassmand4@ovh.net'),
(474, 'Rudd Bodycombe', 'rbodycombed5@360.cn'),
(475, 'Lovell Gillis', 'lgillisd6@booking.com'),
(476, 'Skipper Cloughton', 'scloughtond7@msn.com'),
(477, 'Katya Prickett', 'kprickettd8@timesonline.co.uk'),
(478, 'Klara Byng', 'kbyngd9@imdb.com'),
(479, 'Roi Wetheril', 'rwetherilda@pagesperso-orange.fr'),
(480, 'Eryn Carluccio', 'ecarlucciodb@weibo.com'),
(481, 'Sacha Burree', 'sburreedc@shinystat.com'),
(482, 'Nealy Marland', 'nmarlanddd@comsenz.com'),
(483, 'Nara Farloe', 'nfarloede@meetup.com'),
(484, 'Melvin Yashunin', 'myashunindf@de.vu'),
(485, 'Kingsley Yakovliv', 'kyakovlivdg@eepurl.com'),
(486, 'Carlen Streader', 'cstreaderdh@quantcast.com'),
(487, 'Andy Bradder', 'abradderdi@unesco.org'),
(488, 'Cyndy Bonett', 'cbonettdj@yale.edu'),
(489, 'Ephrem Craghead', 'ecragheaddk@dell.com'),
(490, 'Benyamin Snow', 'bsnowdl@friendfeed.com'),
(491, 'Alfreda Meggison', 'ameggisondm@patch.com'),
(492, 'Frasco Harrop', 'fharropdn@ifeng.com'),
(493, 'Jobye Segeswoeth', 'jsegeswoethdo@cnet.com'),
(494, 'Idaline Keegan', 'ikeegandp@google.es'),
(495, 'Isaiah Waistall', 'iwaistalldq@shutterfly.com'),
(496, 'Ryley Cellier', 'rcellierdr@blog.com'),
(497, 'Jo d\'Arcy', 'jdarcyds@microsoft.com'),
(498, 'Carolina Hunting', 'chuntingdt@businessinsider.com'),
(499, 'Louella Wilshaw', 'lwilshawdu@ucoz.com'),
(500, 'Shayne Garatty', 'sgarattydv@unblog.fr'),
(501, 'William Phillips', 'wp3778q@greenwich.ac.uk'),
(502, 'Scott Test', 'test@test.com');

-- --------------------------------------------------------

--
-- Table structure for table `gsuElection`
--

CREATE TABLE `gsuElection` (
  `electionID` int(11) NOT NULL,
  `electionStartTime` datetime NOT NULL,
  `electionEndTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `gsuElection`
--

INSERT INTO `gsuElection` (`electionID`, `electionStartTime`, `electionEndTime`) VALUES
(1, '2020-01-17 00:00:00', '2020-03-01 00:00:00'),
(2, '2020-01-20 00:00:00', '2021-01-20 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `gsuElectionVotes`
--

CREATE TABLE `gsuElectionVotes` (
  `voteID` int(11) NOT NULL,
  `studentID` int(11) NOT NULL,
  `electionID` int(11) NOT NULL,
  `positionID` int(11) NOT NULL,
  `firstVoteCandidateID_FK` int(11) DEFAULT NULL,
  `secondVoteCandidateID_FK` int(11) DEFAULT NULL,
  `thirdVoteCandidateID_FK` int(11) DEFAULT NULL,
  `fourthVoteCandidateID_FK` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `gsuElectionVotes`
--

INSERT INTO `gsuElectionVotes` (`voteID`, `studentID`, `electionID`, `positionID`, `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK`) VALUES
(1, 1, 1, 1, 19, 203, 52, 169),
(2, 2, 1, 1, 19, 169, 203, 52),
(3, 3, 1, 1, 203, 52, 169, 19),
(4, 4, 1, 1, 169, 203, 52, 19),
(5, 5, 1, 1, 203, 19, 169, 52),
(6, 6, 1, 1, 19, 203, 169, 52),
(7, 7, 1, 1, 169, 52, 19, 203),
(8, 8, 1, 1, 19, 203, 169, 52),
(9, 9, 1, 1, 203, 19, 52, 169),
(10, 10, 1, 1, 203, 52, 169, 19),
(11, 11, 1, 1, 203, 169, 52, 19),
(12, 12, 1, 1, 169, 203, 52, 19),
(13, 13, 1, 1, 19, 203, 169, 52),
(14, 14, 1, 1, 169, 203, 19, 52),
(15, 15, 1, 1, 169, 203, 19, 52),
(16, 16, 1, 1, 203, 19, 52, 169),
(17, 17, 1, 1, 52, 19, 169, 203),
(18, 18, 1, 1, 203, 19, 52, 169),
(19, 19, 1, 1, 203, 52, 169, 19),
(20, 20, 1, 1, 203, 169, 52, 19),
(21, 21, 1, 1, 19, 169, 203, 52),
(22, 22, 1, 1, 52, 203, 169, 19),
(23, 23, 1, 1, 52, 19, 203, 169),
(24, 24, 1, 1, 19, 203, 169, 52),
(25, 25, 1, 1, 169, 52, 203, 19),
(26, 26, 1, 1, 52, 19, 203, 169),
(27, 1, 1, 2, 44, 411, 84, 99),
(28, 2, 1, 2, 99, 411, 84, 44),
(29, 3, 1, 2, 84, 99, 411, 44),
(30, 4, 1, 2, 411, 84, 44, 99),
(31, 5, 1, 2, 44, 411, 84, 99),
(32, 6, 1, 2, 411, 44, 84, 99),
(33, 7, 1, 2, 44, 411, 99, 84),
(34, 8, 1, 2, 99, 84, 411, 44),
(35, 9, 1, 2, 411, 84, 99, 44),
(36, 10, 1, 2, 44, 84, 411, 99),
(37, 11, 1, 2, 99, 411, 84, 44),
(38, 12, 1, 2, 99, 411, 84, 44),
(39, 13, 1, 2, 44, 411, 99, 84),
(40, 14, 1, 2, 84, 44, 411, 99),
(41, 15, 1, 2, 411, 44, 84, 99),
(42, 16, 1, 2, 44, 84, 411, 99),
(43, 17, 1, 2, 99, 411, 44, 84),
(44, 18, 1, 2, 84, 411, 99, 44),
(45, 19, 1, 2, 99, 411, 84, 44),
(46, 20, 1, 2, 84, 99, 411, 44),
(47, 21, 1, 2, 411, 84, 44, 99),
(48, 22, 1, 2, 44, 411, 84, 99),
(49, 23, 1, 2, 411, 44, 84, 99),
(50, 24, 1, 2, 44, 411, 99, 84),
(51, 25, 1, 2, 99, 84, 411, 44),
(52, 26, 1, 2, 411, 84, 99, 44),
(53, 1, 1, 3, 346, 333, 1, 413),
(54, 2, 1, 3, 333, 1, 346, 413),
(55, 3, 1, 3, 333, 413, 346, 1),
(56, 4, 1, 3, 1, 413, 346, 333),
(57, 5, 1, 3, 346, 1, 333, 413),
(58, 6, 1, 3, 1, 333, 346, 413),
(59, 7, 1, 3, 1, 346, 333, 413),
(60, 8, 1, 3, 413, 346, 1, 333),
(61, 9, 1, 3, 413, 1, 333, 346),
(62, 10, 1, 3, 333, 1, 413, 346),
(63, 11, 1, 3, 413, 1, 346, 333),
(64, 12, 1, 3, 333, 413, 1, 346),
(65, 13, 1, 3, 413, 346, 333, 1),
(66, 14, 1, 3, 346, 333, 1, 413),
(67, 15, 1, 3, 346, 333, 1, 413),
(68, 16, 1, 3, 333, 1, 346, 413),
(69, 17, 1, 3, 333, 413, 346, 1),
(70, 18, 1, 3, 1, 413, 346, 333),
(71, 19, 1, 3, 346, 1, 333, 413),
(72, 20, 1, 3, 346, 1, 413, 333),
(73, 21, 1, 3, 333, 413, 346, 1),
(74, 22, 1, 3, 333, 413, 1, 346),
(75, 23, 1, 3, 333, 413, 346, 1),
(76, 24, 1, 3, 333, 413, 1, 346),
(77, 25, 1, 3, 346, 333, 1, 413),
(78, 26, 1, 3, 346, 333, 1, 413),
(79, 4, 1, 6, 412, 473, 251, 144),
(80, 1, 1, 4, 231, 371, 415, 460),
(81, 1, 1, 6, 412, 144, 251, 473),
(82, 1, 1, 5, 312, 25, 360, 123),
(83, 1, 1, 7, 486, 143, 338, 160),
(84, 1, 1, 8, 410, 402, 386, 107),
(85, 1, 1, 9, 116, 487, 450, 300),
(93, 1, 1, 10, 481, NULL, NULL, NULL),
(94, 1, 1, 11, 8, 490, 151, 132),
(95, 1, 1, 12, 26, 111, 478, 269);

-- --------------------------------------------------------

--
-- Table structure for table `gsuPositions`
--

CREATE TABLE `gsuPositions` (
  `positionID` int(11) NOT NULL,
  `positionTitle` tinytext COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `gsuPositions`
--

INSERT INTO `gsuPositions` (`positionID`, `positionTitle`) VALUES
(1, 'President'),
(2, 'Primary GSU Officer'),
(3, 'Secondary GSU Officer'),
(4, 'Tertiary GSU Officer'),
(5, 'Faculty of Liberal Arts and Sciences Officer'),
(6, 'Faculty of Liberal Arts and Sciences Officer'),
(7, 'Faculty of Liberal Arts and Sciences Officer'),
(8, 'Faculty of Liberal Arts and Sciences Officer'),
(9, 'Business School Faculty Officer'),
(10, 'Business School Faculty Officer'),
(11, 'Business School Faculty Officer'),
(12, 'Business School Faculty Officer'),
(13, 'Faculty of Education and Health Officer'),
(14, 'Faculty of Education and Health Officer'),
(15, 'Faculty of Education and Health Officer'),
(16, 'Faculty of Education and Health Officer'),
(17, 'Faculty of Engineering and Science Officer'),
(18, 'Faculty of Engineering and Science Officer'),
(19, 'Faculty of Engineering and Science Officer'),
(20, 'Faculty of Engineering and Science Officer');

-- --------------------------------------------------------

--
-- Table structure for table `studentVoters`
--

CREATE TABLE `studentVoters` (
  `studentID` int(11) NOT NULL,
  `studentLogin` text COLLATE utf8mb4_unicode_ci,
  `studentPassword` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `studentSalt` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `studentVoters`
--

INSERT INTO `studentVoters` (`studentID`, `studentLogin`, `studentPassword`, `studentSalt`) VALUES
(1, 'Test', 'c2df1254bc9f064d87ca2cc953b906112b7fd425f0a05982b9ef640a051cecc374acb49fc2cfbf83d4fdb39179d2f108bfed478fd62d333a5dff1ad3982f381a', '1e3034d9251c13ae1c426bbe383178654870ebd584dadd0ded71c4c43a6311d2'),
(2, 'Test1', '02d2810c323a94642d56cd8797ec21179635a4ace8d063c58dbb88dbf98dd547f4963d7d3fe8aa218b5c05cab149ff03e2cd463c19a81781ab8229e1188c9083', '2105ecd2120c8700db2c0f1afdefe68fb395fe72a27954b11d797543a46c083f'),
(3, 'Test2', 'd654be2f78ca18b30d924b0c8341801dd2af4fe8db1baab357ef276237e3d5ca7a16795caf8f7883f9971a269a973d9803df9c4d3a7a905d7af82ad305670194', 'f7fbf582986e67633369e9f7dd804a21ef1a128907c5af4d5531f268f3a21a22'),
(4, 'Test3', '9bd79c0797fceaa5665dc95945233ab48d109f34550eb0e00dadb698a9bf230d42012da2930f20cb56783096cddce7c7188b698f328f0e476d353601b47c8164', 'd75f23b40d55a47c81d3982ffbd2ce19ec5f23593bfa3ac9c4348d6a93cbe507'),
(5, 'Test4', 'b79659f879e86afb7d12c1be943c9cd98efadc5a5cf70d209e1ad4f994f172c20b0de6a560333d6aa558dd0347b723524fd2be8ea6b7688925eb54de5bd3881a', '12e28f90c153c78a2756ef29b75f0c9c3bd950da84329270b632560459516d28'),
(6, 'Test5', 'e5b49c708feea4f979004dd0c79c673e9a66b8ab5ecd14a624837ae44cc8ce7f66dd79ef43188170b63cb7419e1968b0881004bac61961e4d897695adf903627', '99b6424310e5bd624064ab56719cd64ad491da7e5846fb1d78aff6c6a3923b29'),
(7, 'Test6', 'fc6e0f1db4aa550a6a831e4f9887e6217b6cdca6b461cdff97080e928452cb13d63f7e1bd2b09162d556d2265626ddac3c70b690a35e016cf94c98c36c9c71b9', '6be1e355fa7e1ff53eb5767a7d5c55f6047693912b32299ea2993d6fdebb3e1d'),
(8, 'Test7', '0281c192cf079f4ea6449907a6db1b79272bde5b08723da975275ffb6aa0526e96a3288abb964eb0728525d2a1a473cf2a27b66528ede8d2b625ed41f3a688f0', '97e8f0f8a48dad062d803116c45d29b45739594e7ea1bd137470a43debbef5cb'),
(9, 'Test8', '23cc27019877611e8a71681831c688196ab5bf974ffef6dc229222ee7e56a3e39b5608d31885afd540abdbde5fee762abdfc33a0ba4a608ec3d66998be89ff43', '6ea5e28556dc75503043414822f9fb94c5a2ef58d3da436517f622a1c60c5ce5'),
(10, 'Test9', '104077f984ffec6ff6a4d42b8082e7531fb015e6e11cc586f2fe5f278ae7064320ac270ee45453f343fa589ff1df1b5f6d79232a9d7b13838b8f874a8bbbbbc6', 'e0075893988e1f3c41ade9aed807438f975042a400922030a204ea39daf32bed'),
(11, 'Test10', 'b0aa97e001818ab39ca11e20528fa8c05acb80c04fac9e2bd749244864be011d85d14db386d5b4f9d3382438a2bb2f7499dc9ee145a2e880813f4bd5783fd623', '030377dedcdeda9f081029e151aa5012f4da3da8a6d83cd2db2cfed647d2ffca'),
(12, 'Test11', '9657f6de5c01184dc3f9091330a14798cf8a2cdf9a6c0a12c32d642bd0e485afac0db80f828cd5b515049a25ab1be548a3076b7a6ffa82d9f840ee2c0d7c17a2', 'f4459aa7d7dbd43672e12dd8b1f9b9a3d1319407b7a66b4480f1069b856d18ff'),
(13, 'Test12', 'c605fe974d5fa1d3f2602cbbe857fc6de744649e2579ead420a5209d2822034d58f435967961073a211b2d78a488cee0f8ec8a17ff346521e0d6186cf6f9536f', 'f7a1a1dbec9ed41288166b8b840ee941f23b0a52bb03be3f231b6ac99ed9778e'),
(14, 'Test13', 'c0b18f7f941737643ec7a4a9b0811ba88ce6673e42e1f77ff59c14c1383162a8ad5b403b6c320b7b5a3fa024205268cee59f32e8b2027e7e8c1d5200079b6c26', 'df6287e99c5b6ae4c16b2f70915ceda5bde91731f703dc682329802807837a3e'),
(15, 'Test14', '262b8686ef74da9873976b90b082f675e01f76a38d789e78b777f155b724c587fefc528b034ab5cb2f2b6826ca95feb70bcf0508e7b7cbb56425f23ffc22bb13', '105a5fafc562cdba084919a321f10d0df6dd604492cc8e0dae4af5fb5fb41015'),
(16, 'Test15', '6147d03290d8a08cdc1bbb6498f3e3e60c171c140e79fc4a7834e5f05dff197b74e5fd61ccb0c11404d05fc3cd4caafc30a798cdb0a3e3da8b15e71502d1e891', 'fa27a7cceade3f132e0cea863d84e84d9b153173fdaf8acb55604fe2d1b5cb6c'),
(17, 'Test16', '1344d73d18ede788a4cb1731524a77c182140eed6de52bbc6ff4a91bfd43bed7e92f293219a61d6e6031577cc8695eead03ba67fc92275ff48ad8000982b8979', '598dfd6710a9ba4f6f9d7f381d7982a2ff662150766c70310991236cafa58831'),
(18, 'Test17', 'bf60274bf87484943fb42faf74102fcbefaf9bd1d0a93b104aab5948e8ba85587728b5601c693141287dbada3c1cd908dc451be636905fc47c494c448c27f3df', '5100f72db3b8a8643bf477116b87d8349bbb501034f81d3dea432159ab836e35'),
(19, 'Test18', '6b7c63b24287b6445f22a498208ae132bca655374305d8527ee248789a2e400de86cf2188a8e32937222252cf4e4d000c600e326dd7c253c5166566c546b92e6', '6b72582f1b3c8a1777a7550cb1e59f7f2065cec3cb32ab89521fae7fbeca8915'),
(20, 'Test19', 'e35251fafa2869dfd1e97b8c706bd4b95a822c636c66cf0c595376d4f9caf8d4436d142e194bb149f52abc24ec74f04058fe2a5e297307b759d5f0c8c4bfe12a', '5b8848759f449f1411f447bb09cba57cb6248793b4f40646539195bcacb48644'),
(21, 'Test20', '81cfab3c5613a5fcec2ece567f3c658dd2c819be63bac522051f549eec6cb7fd7176082fb48ef0ac9581f8b26ccb3e9640ab4e89c8a6f4a9a21ae6cb7ea9c5a2', '2aa1a0e914f3bd59d04c2a7e3f1c0364d047d3e4c4e27437bd220c7c7311b7f5'),
(22, 'Test21', '065442ae4fdfe2e22573a4bd47811dd86572626098405986f152bcc46606c43d3cc84432e5aaeacda87f39e3c690fe292c5ce09dfccf1965cdae661ec6a9b282', '3bfd4f7ae957c6edd0a95caadebd725635ff164afdd657e3fbf2fe496fe400f5'),
(23, 'Test22', '06a1103dc9e13ae2a5940a82482d73d8f4a31d9cfda27af4505474d62f4c234aee16515c01eb7ea52b7e5f9eee4ad6a39747b111c6ffeae895a5380ad71290b4', 'e60cfdb5415ec9e3a443bf8ef890c3b33879c6770ff00f111492529af608f756'),
(24, 'Test23', '0cb5c3e1ed9ba0477253d35b2021d8441fd46f8260effbf8eaf1836a3252f081d2177e52b5d06a5472f50681a9cf4fe8da1ea52bfee1cce17ecadceaf757b5b8', '80941a30cae62ae8e5a6dfabb4633a7bfe37877a5d03fd775f952a5f24b48b00'),
(25, 'Test24', '41dc1968a0229f50981a95cf05a2a4abfce57a2d00adb8b64dc5a7f85baca3e6f42c698944d0fef95b7d5ee611257b0ef2d6c0d1fca4187e7d3a5797fe8c0d5b', '41a8b9b724708286ead5c1cf00ac0d3d94c778f98d5cc8744c58501dd5abc1a2'),
(26, 'Test26', '6e4ba4113b9222af84dd4ad9a375de1e4890df83131210ce9cf0e776c4cd47ad09520ea2e316966f6bb5e1170d9fcf1bc1d20297aeb436bc622957eb5f543d3f', '6710933a375dd80880ce4cd146546af675f825d903e782f09bf8b47ecadc934c'),
(27, 'Test27', 'ad8f4b16101d71276b692595108750163e4775b9df974becfa30c6f8606db308128568076bcaa666e9f1303b07849d59972eb206bb43933fb5748526092daf57', '4ebf50518f5eefbb1a7ff21e4a83dc290c8223e2165344696e7eba8694020ab6'),
(28, 'Test28', 'e205c2db229899709e103331b2829973ac6fade196587fbbf1d9017fc6944e5f34eb56c4104dcec077a96db1c8cc8fb6fd6886e1f090fd0665a2a3cd23dd0694', 'fa5f90954c8d8dcee2f5ead8baa60e383b0ea0fd1760e3e49cf465cceab9833f'),
(29, '', 'b01b8e4960aaa03c17cbd767c5b2007b04b21eed2d7bb1b0e13298423bd1bac50c070b1676f299b587322a81e84c83c191ac9524382520996639c16cfea0db05', '1feddb57890a8a524e4bc1df28c70e6b9916af054f3390033a225ede2eba04ba'),
(30, 'Test72', 'c34c9c2a5a7728690f6fc9e1931c4d58f521832063874104094d6b86c0d7db47cb7b5eada0a8afae4573aac4908acfa1ee45239691bcf386ed36d501b8b39eec', 'cbcc9bc98f23cf85c9b4107e1c631c46436190931afc59fb9dd4fe1c89be1405'),
(31, 'Brian', 'a0e68e99950e20b46be0fab43a3cd9309881d86d01ddd523c9e96f275c361162613c1553c679f7c5e3cf8cffbb5eec1f1ade591e8cf9661503ede29bc6fff1b1', 'd6d00465b50c54e4d6d385cd74cc64fc71c6dbe2aa2f58d89bb6dffac908cb2d');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gsuCandidateApplication`
--
ALTER TABLE `gsuCandidateApplication`
  ADD PRIMARY KEY (`applicationID`),
  ADD KEY `candidateID` (`candidateID`),
  ADD KEY `positionID` (`positionID`),
  ADD KEY `electionID_FK` (`electionID`);

--
-- Indexes for table `gsuCandidates`
--
ALTER TABLE `gsuCandidates`
  ADD PRIMARY KEY (`candidateID`);

--
-- Indexes for table `gsuElection`
--
ALTER TABLE `gsuElection`
  ADD PRIMARY KEY (`electionID`);

--
-- Indexes for table `gsuElectionVotes`
--
ALTER TABLE `gsuElectionVotes`
  ADD PRIMARY KEY (`voteID`),
  ADD KEY `firstVote` (`firstVoteCandidateID_FK`),
  ADD KEY `secondVote` (`secondVoteCandidateID_FK`),
  ADD KEY `thirdVote` (`thirdVoteCandidateID_FK`),
  ADD KEY `fourthVote` (`fourthVoteCandidateID_FK`),
  ADD KEY `electionID` (`electionID`),
  ADD KEY `positionID_FK` (`positionID`),
  ADD KEY `studentID` (`studentID`);

--
-- Indexes for table `gsuPositions`
--
ALTER TABLE `gsuPositions`
  ADD PRIMARY KEY (`positionID`);

--
-- Indexes for table `studentVoters`
--
ALTER TABLE `studentVoters`
  ADD PRIMARY KEY (`studentID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gsuCandidateApplication`
--
ALTER TABLE `gsuCandidateApplication`
  MODIFY `applicationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `gsuCandidates`
--
ALTER TABLE `gsuCandidates`
  MODIFY `candidateID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=503;

--
-- AUTO_INCREMENT for table `gsuElection`
--
ALTER TABLE `gsuElection`
  MODIFY `electionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `gsuElectionVotes`
--
ALTER TABLE `gsuElectionVotes`
  MODIFY `voteID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=96;

--
-- AUTO_INCREMENT for table `gsuPositions`
--
ALTER TABLE `gsuPositions`
  MODIFY `positionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `studentVoters`
--
ALTER TABLE `studentVoters`
  MODIFY `studentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `gsuCandidateApplication`
--
ALTER TABLE `gsuCandidateApplication`
  ADD CONSTRAINT `candidateID` FOREIGN KEY (`candidateID`) REFERENCES `gsuCandidates` (`candidateID`),
  ADD CONSTRAINT `electionID_FK` FOREIGN KEY (`electionID`) REFERENCES `gsuElection` (`electionID`),
  ADD CONSTRAINT `positionID` FOREIGN KEY (`positionID`) REFERENCES `gsuPositions` (`positionID`);

--
-- Constraints for table `gsuElectionVotes`
--
ALTER TABLE `gsuElectionVotes`
  ADD CONSTRAINT `electionID` FOREIGN KEY (`electionID`) REFERENCES `gsuElection` (`electionID`),
  ADD CONSTRAINT `firstVote` FOREIGN KEY (`firstVoteCandidateID_FK`) REFERENCES `gsuCandidates` (`candidateID`),
  ADD CONSTRAINT `fourthVote` FOREIGN KEY (`fourthVoteCandidateID_FK`) REFERENCES `gsuCandidates` (`candidateID`),
  ADD CONSTRAINT `positionID_FK` FOREIGN KEY (`positionID`) REFERENCES `gsuPositions` (`positionID`),
  ADD CONSTRAINT `secondVote` FOREIGN KEY (`secondVoteCandidateID_FK`) REFERENCES `gsuCandidates` (`candidateID`),
  ADD CONSTRAINT `studentID` FOREIGN KEY (`studentID`) REFERENCES `studentVoters` (`studentID`),
  ADD CONSTRAINT `thirdVote` FOREIGN KEY (`thirdVoteCandidateID_FK`) REFERENCES `gsuCandidates` (`candidateID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
