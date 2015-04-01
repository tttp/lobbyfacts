#!/usr/bin/env python
# -*- coding: utf-8 -*-

uuids = [ (u'President Jean-Claude Juncker', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=829436d0-1850-424f-aebe-6dd76c793be2'),
          (u'Cabinet members of President Jean-Claude Juncker', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=91b45ce8-2ff0-4e67-b5b5-b42151217f13&d-6679426-p='),
          (u'First Vice-President Frans Timmermans', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=b47bf526-b773-40e7-9392-89d454e0672f'),
          (u'Cabinet members of First Vice-President Frans Timmermans', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=f3715246-e6ff-4856-b9d8-1ed4f86738b7'),
          (u'High Representative/Vice-President Federica Mogherini', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=6e27e5b2-65cf-4733-99b1-0a5e094088c1'),
          (u'Cabinet members of High Representative/Vice-President Federica Mogherini', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=b6c0bf49-dbd0-4884-af38-d0da75bc6395'),
          (u'Vice-President Kristalina Georgieva', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=5270d9e0-5945-4d88-99c0-5dfc4757503e'),
          (u'Cabinet members of Vice-President Kristalina Georgieva', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=bd40b1da-482e-472a-8d00-fcb21ed47880'),
          (u'Vice-President Andrus Ansip', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=57870d0f-2fb5-4f5b-9bea-7f2a661c64ac'),
          (u'Cabinet members of Vice-President Andrus Ansip', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=cd3770a0-4fb5-4e79-a343-072b167456b3'),
          (u'Vice-President Maro\u0161 \u0160ef\u010dovi\u010d', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=a7c58a45-8006-46df-9f12-b80ff5b34a1f'),
          (u'Cabinet members of Vice-President Maro\u0161 \u0160ef\u010dovi\u010d', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=dea9b479-804b-4eb7-92cd-f0ebc6a445d1'),
          (u'Vice-President Valdis Dombrovskis', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=12405586-0ba8-4a54-94ae-12e8daeb7b26'),
          (u'Cabinet members of Vice-President Valdis Dombrovskis', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e6418b8f-9cc0-44ab-9818-a40997dea82e'),
          (u'Vice-President Jyrki Katainen', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=d4efd679-b6bf-4ef8-a077-a041991378c7'),
          (u'Cabinet members of Vice-President Jyrki Katainen', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=11408bf9-1c96-46d1-803f-5852821362dd'),
          (u'Commissioner G\xfcnther Oettinger', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=f24e4f06-d181-4f58-9604-3aaf3ce391ea'),
          (u'Cabinet members of Commissioner G\xfcnther Oettinger', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=595cf53f-c018-4fc8-afa0-9d66c289795c'),
          (u'Commissioner Johannes Hahn', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=92703759-b346-49b5-83ac-edf2bbe01d2f'),
          (u'Cabinet members of Commissioner Johannes Hahn', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=dee51db7-bb13-4d5e-a753-43f58a567da2'),
          (u'Commissioner Cecilia Malmstr\xf6m', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=fdf6c08d-54d1-4524-aa70-1287c34ceb4d'),
          (u'Cabinet members of Commissioner Cecilia Malmstr\xf6m', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=61aa8586-2b0d-4394-b196-30c13f1fa663'),
          (u'Commissioner Neven Mimica', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=682fd8b6-7fce-4fba-91af-525e4a9cbf52'),
          (u'Cabinet members of Commissioner Neven Mimica', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=b63071fc-cabe-4ca8-ae34-a28182ee77e9'),
          (u'Commissioner Miguel Arias Ca\xf1ete', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=523060f7-97c6-480b-8bb9-30bb409e650e'),
          (u'Cabinet members of Commissioner Miguel Arias Ca\xf1ete', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=9778d998-6aed-40e3-a1d6-614db81c7918'),
          (u'Commissioner Karmenu Vella', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=f92a74d6-757c-46fd-8042-2564cc3d763f'),
          (u'Cabinet members of Commissioner Karmenu Vella', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=0fbb66b7-d3ed-44b7-9ddc-6fcc02880a75'),
          (u'Commissioner Vytenis Andriukaitis', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=a980459e-c697-49b1-9713-5c5034a26cdc'),
          (u'Cabinet members of Commissioner Vytenis Andriukaitis', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e59c4da1-3434-4ddf-aa47-ade4c7dd0396'),
          (u'Commissioner Dimitris Avramopoulos', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=1b4b07a3-f945-456c-a005-6546de4bf468'),
          (u'Cabinet members of Commissioner Dimitris Avramopoulos', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e2d6f6f8-a020-4a91-b127-37f543c30e5b'),
          (u'Commissioner Marianne Thyssen', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=3aaa2b0d-1706-495f-9c93-7f939888afb2'),
          (u'Cabinet members of Commissioner Marianne Thyssen', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=0cbf10a4-0ceb-4eee-a8ff-cb4a7d0c12d1'),
          (u'Commissioner Pierre Moscovici', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=af65fb60-5ba8-4af1-87ae-edab5dac6afa'),
          (u'Cabinet members of Commissioner Pierre Moscovici', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=f033c462-1999-46a6-bc20-41681b6ee898'),
          (u'Commissioner Christos Stylianides', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=7a3ad6a0-2fdd-4656-8462-85f57d9a8c54'),
          (u'Cabinet members of Commissioner Christos Stylianides', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=c8069fd5-5ab9-4ecb-ae1f-7e4961724890'),
          (u'Commissioner Phil Hogan', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=55ddae5a-33fa-40b4-87b4-8815e503dc26'),
          (u'Cabinet members of Commissioner Phil Hogan', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=93d7d7cd-b3d3-4b15-9d6c-e260103bde3a'),
          (u'Commissioner Jonathan Hill', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=ebb93164-c494-436e-b965-e367adbcae32'),
          (u'Cabinet members of Commissioner Jonathan Hill', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=8f89f28d-f775-4807-b9d0-606199b7855b'),
          (u'Commissioner Violeta Bulc', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=8d390599-609a-4464-b941-6815b1228b44'),
          (u'Cabinet members of Commissioner Violeta Bulc', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=6c292f99-8c7f-4d91-a8ff-6aeef35a9375'),
          (u'Commissioner El\u017cbieta Bie\u0144kowska', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e8354e80-dd05-4cb8-ba46-0dbb02ee2d88'),
          (u'Cabinet members of Commissioner El\u017cbieta Bie\u0144kowska', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=85ded49b-f5bb-486e-9404-b864a34d8340'),
          (u'Commissioner V\u011bra Jourov\xe1', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=cc463fab-bfff-4595-bb45-6d0af96b5e83'),
          (u'Cabinet members of Commissioner V\u011bra Jourov\xe1', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=2bca07c7-d7fa-4e18-9d9d-104e3af20e2f'),
          (u'Commissioner Tibor Navracsics', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=bba8a7ac-cad1-4ac5-815a-1abdff5f51b1'),
          (u'Cabinet members of Commissioner Tibor Navracsics', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=52964d39-1350-42fa-94ec-8a58d5fa86b2'),
          (u'Commissioner Corina Cre\u021bu', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=aa125a9c-d202-490d-865e-758d5df2f01d'),
          (u'Cabinet members of Commissioner Corina Cre\u021bu', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=b1991508-f1ca-473a-b633-4b308b341a92'),
          (u'Commissioner Margrethe Vestager', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=46942686-5de0-426c-9d77-decc4e003a84'),
          (u'Cabinet members of Commissioner Margrethe Vestager', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=74d81d51-18b9-4a85-8983-b26b42f4efe5'),
          (u'Commissioner Carlos Moedas', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=375218b1-5b9b-4f1f-8701-cda656622c9a'),
          (u'Cabinet members of Commissioner Carlos Moedas', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=39401b95-74dc-4360-8ce2-aca281bc05c1'),
          (u'Director-General Rytis Martikonis', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=0fbdad0a-4342-4091-b766-91b393b97617'),
          (u'Director-General Jerzy Bogdan Plewa', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e5538979-4674-413c-9912-75853e91bdc5'),
          (u'Director-General Nadia Maria Calvino Santamaria', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=1eefac79-31f7-41ef-b1f0-3d1270ce33a9'),
          (u'Director-General Jos Delbeke', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=d41e42be-7ff1-4635-bb4f-e47d38f886ed'),
          (u'Director-General Gregory Paulger', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=96774901-848c-400f-a005-0a51d74dede7'),
          (u'Director-General Robert Madelin', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=aae7124c-b839-4139-9ffe-ad5660fe9404'),
          (u'Director-General Alexander Italianer', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=ffdb1b81-84a9-4ce1-8974-164aa26ce7e8'),
          (u'Director-General Marco Buti', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e2ac53f7-cf9c-4aa7-a7fd-06a355c8b361'),
          (u'Director-General Michel Servoz', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=6c877f62-58d1-4645-aa27-bbbc7b872de3'),
          (u'Director-General Dominique Ristori', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=61569260-525e-42f8-aa52-51d7bfc30d4f'),
          (u'Director-General Karl-Friedrich Falkenberg', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=ca175ad3-c2c5-457e-8f6d-f17956bdcc4e'),
          (u'Director-General Jonathan Faull', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=1451b45a-b39b-48ee-a50a-00a440ef2f09'),
          (u'Director-General Ladislav Miko', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=357c8eea-da5c-49bc-9d63-a5c1b76c770e'),
          (u'Director-General Daniel Calleja Crespo', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=66b9a93e-bac3-4820-8f21-9576b54e3428'),
          (u'Director-General Fernando Frutuoso de Melo', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=19bd5d17-a3ef-4a2b-899c-28126a38b0c2'),
          (u'Director-General Vladimir \u0160ucha', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=30674a4b-0bbe-4243-9500-704f334ced64'),
          (u'Director-General Lowri Evans', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=0bdcfdaf-b25f-4fa4-9843-6d8aff622df9'),
          (u'Director-General Alfred Matthias Ruete', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=4a2b905b-d91f-421a-870a-3f9387018669'),
          (u'Director-General Christian Danielsson', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=e780754a-50f5-41fe-b42f-8ffe6165ad35'),
          (u'Director-General Walter Deffaa', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=836198d9-3839-4b03-861c-7d7b2dc923bf'),
          (u'Director-General Robert-Jan Smits', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=9c8a817a-8b63-494f-b8aa-7f1d9a3d4aa7'),
          (u'Director-General Heinz Zourek', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=8d411331-1f9c-49ad-bf3f-54c9723c5496'),
          (u'Director-General Jean-Luc Demarty', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=5f4689e0-014c-4bec-8125-f9e6d3592c86'),
          (u'Director-General Stephen Quest', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=06fb3b80-76a8-43f1-b1a5-e703cfe8d625'),
          (u'Director-General Paraskevi MICHOU', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=b7f75e74-dd34-4911-8942-3b84e241424d'),
          (u'Director-General Joao Aguiar Machado', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=ed82401c-d412-44bd-bdbc-3d0c5d051337'),
          (u'Director-General Walter Radermacher', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=b85b3c8d-483b-4e3d-b066-160c467e2884'),
          (u'Director-General Xavier Prats Monn\xe9', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=9bd9f7c0-836e-4ff6-abf4-a1f8650861cb'),
          (u'Director-General Ann Mettler', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=0d0d638f-322e-44fc-8c9c-875438c4a719'),
          (u'Secretary-General Catherine Day', u'http://ec.europa.eu/transparencyinitiative/meetings/meeting.do?host=394df231-6f63-43a1-ac2f-a5c6c2aea0b7') ]

entmap = {
    u'NEREUS - Network of European Regions Using Space Technologies': (u'NEREUS - Network of European Regions Using Space Technologies', '894707011106-07'),
    u'Air France': (u'AIR FRANCE','350652449-83'),
    u'Association Française des Entreprises Privées': (u'Association Française des Entreprises Privées','953933297-85'),
    u'Association of British Insurers': (u'Association of British Insurers','730137075-36'),
    u'Edison': (u'Edison Spa', '401111262-07'),
    u'EDISON': (u'Edison Spa', '401111262-07'),
    u'Edison Spa': (u'Edison Spa', '401111262-07'),
    u'EDISON Spa': (u'Edison Spa', '401111262-07'),
    u'European Football Agents Association': (u'European Football Agents Association', '502023615731-55'),
    u'European Logistics Association': (u'European Logistics Association', '486101215470-41'),
    u'European Organisation for Rare Disease': (u'EUROPEAN ORGANISATION FOR RARE DISEASES', '93272076510-87'),
    u'Federation of European Publishers': (u'Federation of European Publishers', '398541467-53'),
    u'Independent Retail Europe': (u'Independent Retail Europe (formerly UGAL - Union of Groups of Independent Retailers of Europe)', '034546859-02'),
    u'Independent Retail Europe (formerly UGAL - Union of Groups of Independent Retailers of Europe)': (u'Independent Retail Europe (formerly UGAL - Union of Groups of Independent Retailers of Europe)', '034546859-02'),
    u'PERNOD RICARD': (u'PERNOD RICARD', '352172811-92'),
    u'Telefonica': (u'Telefonica, S.A.', '52431421-12'),
    u'Telefonica, S.A.': (u'Telefonica, S.A.', '52431421-12'),
    u'Transparency International Brussels Liaison office': (u'Transparency International Liaison Office to the European Union', '501222919-71'),
    u'Transparency International Liaison Office to the European Union': (u'Transparency International Liaison Office to the European Union', '501222919-71'),
    u'Transparency International (TI)': (u'Transparency International Liaison Office to the European Union', '501222919-71'),
    u'Transport and Environment': (u'Transport and Environment (European Federation for Transport and Environment)', '58744833263-19'),
    u'Carbon Capture and Storage Association': (u'Carbon Capture & Storage Association', '69382094718-43'),
}
