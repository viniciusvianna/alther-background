SET FOREIGN_KEY_CHECKS = 0;

INSERT INTO ASPIRACOES VALUES 
('OF', 'OFENSOR'),
('DF', 'DEFENSOR'),
('CT', 'CONTROLADOR');

INSERT INTO ESCOLAS VALUES
('PA', 'Peregrinos do Amanhecer'),
('DA', 'Discípulos do Ardente'),
('VC', 'Vingadores do Crepúsculo'),
('AP', 'Adeptos da Prata'),
('DV', 'Desbravadores do Vazio'),
('AV', 'Avimortis'),
('CS', 'Carvisangi');

INSERT INTO RACAS VALUES
('ALT', 'ALTALIA', 'VOAR', 'Altalia podem voar utilizando uma ação de movimento (em
batalha) ou um teste de perícia corporal (fora de batalha). Em
batalha eles podem se manter no ar por um turno sem gastos.
Fora de batalha eles conseguem se manter por 30 min. Estar
voando torna Altalia imunes a ataques rasteiros e concede +2NP
na esquiva contra armas curtas. No entanto, recebem -1NP na
defesa contra ataques de longa distância.', 'DEVORADORES DE CARNE', 'Altalia não conseguem digerir nenhum tipo de planta, nem
mesmo ervas de cura, frutas ou qualquer alimento de origem
vegetal. Caso haja a ingestão, o altalia passa mal, ficando
estafado por um período de 1 a 3 h.'),
('FEN', 'FENÍRIO', 'FARO APURADO', 'Fenírios podem farejar seus inimigos ou aliados. Se um fenírio
tiver contato com um cheiro uma vez, ele pode utilizar essa
habilidade para rastrear seu alvo com sucesso garantido, em
um raio de 20+NP km. Em batalha, esta habilidade pode ser
utilizada como ação padrão e para sentir o cheiro de um
oponente. A partir de então até o fim da batalha o oponente não
pode ficar oculto para o fenírio sem disfarçar seu cheiro.', 'MATILHA', 'Fenírios não se viram bem sozinhos. Caso estejam isolados do
resto de seu bando (que não precisa ser constituído de outros
fenírios), eles recebem -1 de Treinamento em qualquer teste de
perícia de foco e uivam periodicamente, chamando atenção
para si.'),
('GOL', 'GOLLYCK', 'NADO GOLLYCK', 'Gollycks podem utilizar essa habilidade como um teste de
perícia ou como uma ação de movimento em batalha para nadar.
Fora de batalha, esta habilidade concede sucesso garantido em
qualquer teste de nadar e também permite que um gollyck nade
na areia, lodo e terra fofa, além da água. Em batalha, enquanto
nada um gollyck se move duas vezes mais rápido e ganha +NP+5
na defesa contra ataques físicos. Tomar qualquer ação diferente
de nadar tira o gollyck deste estado.', 'FACE DO MEDO', 'Gollycks dificilmente são bem vistos por outras raças. Mesmo
que um gollyck seja bondoso e honesto, ele encontrará
resistência nas interações sociais, até mesmo com membros de
sua própria raça que não tenham crescido com ele. Assim,
recebem -2 de Treinamento em qualquer teste de perícia social.'),
('LOD', 'LODGER', 'MOVIMENTO ÁS', 'Lodgers podem utilizar esta habilidade para obter +2NP em
testes de perícia que envolvam escalada ou equilíbrio. Além
disso, em batalha, eles ganham +1NP em testes de esquiva
contra ataques corpo a corpo. Caso a esquiva seja bemsucedida, eles podem usar uma ação livre de movimento para se
reposicionar.', 'PEQUENINOS', 'Lodgers tem uma constituição muito pequena e, portanto, não
podem utilizar armas longas e equipamentos pesados. Em
compensação, sua elevada destreza permite que eles operem
armas curtas melhor que outras raças, concedendo +1NP no
acerto em ataques com elas.'),
('MAE', 'MAEK', 'DIPLOMACIA MAEK', 'Em batalha, maeks podem usar essa habilidade uma vez para
convencer um inimigo a ajuda-lo, fazendo um teste social
contra a resistência de seus adversários. Esta habilidade só
pode ser utilizada contra raças inteligentes. Além disso, maeks
recebem +1 de Treinamento em perícias sociais.', 'ARTE-VULNERÁVEIS', 'Maeks são mais suscetíveis aos efeitos causados pelo contato
com a energia extradimensional. Eles têm uma penalidade
permanente de -1NP em sua resistência. Além disso, ficam o
dobro de turnos a mais afetados por qualquer efeito artístico.'),
('NUA', 'NUAA', 'SANGUIDOURADO', 'O sangue dos nuaa concede a eles habilidades mágicas únicas.
Toda arte utilizada por eles ganha +1NP no dado de efeito. Caso
a arte possua efeito fixo, eles dobram o seu tempo de duração.', 'CONSTITUIÇÃO FRACA', 'Nuaa não têm corpos muito resistentes e por isso são
altamente suscetíveis à fadiga, venenos, álcool, etc. Todas as
penalidades sofridas em todos esses casos são dobradas para
eles. Além disso, realizar testes de perícia corporal seguidos
concede -1NP de penalidade acumulativo para cada teste
subsequente.'),
('PAI', 'PAISHU', 'BRAÇOS DE GIGANTE', 'Os paishus tem força excepcional quando concentram suas
energias nos seus braços. Assim, eles ganham +1NP de dano em
todos os seus ataques físicos. Além disso, eles podem utilizar
seus braços em uma ação de movimento para andar 2 m a mais
(em batalha) ou ganhar +1 de Treinamento em testes de corpo
(fora de batalha).', 'ENORMEMENTE DENSO', 'Paishus são densos demais para nadar ou se equilibrar com
facilidade. Eles sofrem -2 de Treinamento de penalidade nestes
testes. Em compensação, eles podem aguentar um peso igual a
10 vezes o próprio acima da cabeça.'),
('QUA', 'QUA’DIR', 'HIPERSALTO', 'Qua’dir podem usar esta habilidade como ação de movimento em
uma batalha. Eles saltam até seu movimento normal + 2 m e
ignoram qualquer barreira física de menos de 2+NP m de altura.
Eles conseguem carregar um objeto ou um indivíduo de até 2x
seu próprio peso no salto. Fora de batalha, eles têm sucesso
garantido em testes de perícia que envolvam saltar.', 'HIPERATIVIDADE', 'Qua’dir não conseguem ficar parados por muito tempo. Eles
dormem apenas 4 horas por dia e precisam de algo para se
distrair caso não tenham nada para fazer. Em batalha, eles
devem gastar pelo menos uma ação de movimento por turno.
Caso sejam impedidos de se mover por um fator externo, eles
tomam penalidade de -2NP no dado de acerto de qualquer
ataque que realizem.'),
('RAE', 'RAE', 'PASSO OBSCURO', 'Os rae possuem uma habilidade única de caminhar brevemente
pelo limiar das dimensões. Em batalha, o rae pode utilizar 5
pontos de mente para usar essa habilidade como ação padrão e
ficar invisível para todos os outros que não sejam rae e que não
tenham visão do limiar. Então, ele pode se mover livremente
pelo campo. Sua próxima ação padrão cancela este estado. Fora
de batalha ele pode fazer um teste de perícia mental para andar
invisível. A distância determina a CD do teste.', 'HEMATÓFAGOS', 'Rae se alimentam apenas de sangue animal, porém eles
gostam muito de sangue. Caso um rae veja sangue vermelho
em determinada quantidade ele deve fazer um teste de
resistência. Caso fracasse, o rae estará inebriado e receberá
-2NP nos dados de acerto de suas ações. A cada turno ele deve
refazer o teste, enquanto estiver inebriado.'),
('SAI', 'SAITYR', 'VOZ DA NATUREZA', 'Saityres podem se comunicar com animais, utilizando pontos de
natureza. Em batalha, como uma ação padrão, o saityr pode
comandar um animal selvagem para realizar um ataque simples
contra um inimigo. Animais pequenos: 2 ponto; Médios: 4
pontos; Grandes: 10 pontos; Enormes: 20 pontos; Épicos: 40
pontos; Míticos: 50 pontos. Fora dela, o saityr pode fazer
pedidos simples e ouvir informações simples dos animais
gastando 1 ponto de natureza.', 'CASCOS FENDIDOS', 'Saityres possuem cascos no lugar dos pés e, desta forma, não
conseguem andar em qualquer terreno com facilidade.
Terrenos muito fofos (como a areia do deserto) ou muito
irregulares (como os vales montanhosos) concedem
penalidade de movimento de metade do movimento total do
saityr, em batalha ou não. Além disso, eles recebem -1 de
Treinamento em testes de perícia de foco.');

INSERT INTO CAMINHOS VALUES 
('MON', 'MONGE', 1, '+1dA ACERTO E +4 DE CORPO', '', 'OF'),
('NEB', 'NÉBULO', 1, '+1dA DE ESQUIVA E +4 DE FOCO','', 'OF'),
('ARC', 'ARCANTE', 1, '+1dA DE ARTES E +4 DE MENTE','', 'OF'),
('SHE', 'SHEPIAN', 1, '+1dE DE DANO E +4 DE ESPÍRITO','', 'OF'),
('HAS', 'HASSASSIN', 2, 'SUCESSO GARANTIDO EM 1dA DE
ACERTO, +4 EM CORPO E +4 EM FOCO', 'MONGE Lv 7
NÉBULO Lv 7', 'OF'),
('EVO', 'EVOCADOR', 2, 'SUCESSO GARANTIDO EM 1DA DE
ARTES, +4 EM MENTE E +4 EM ESPÍRITO', 'ARCANTE Lv 7
SHEPIAN Lv 7', 'OF'),
('ARA', 'ARAUTO', 2, 'SUCESSO GARANTIDO EM 1DA DE
DANO, +4 EM CORPO E +4 EM ESPÍRITO', 'MONGE Lv 7
SHEPIAN Lv 7', 'OF'),
('ACE', 'ACE', 2, 'SUCESSO GARANTIDO EM 1DA DE ESQUIVA, +4
EM MENTE E +4 EM FOCO', 'ARCANTE Lv 7
NÉBULO Lv 7', 'OF'),
('CRU', 'CRUZADO', 1, '+1dA DE DEFESA E +4 DE CORPO', '', 'DF'),
('BAR', 'BARDO', 1, '+1dA DE ESQUIVA E +4 DE FOCO', '', 'DF'),
('DRU', 'DRUIDA', 1, '+1dA DE ARTES E +4 DE MENTE', '', 'DF'),
('PAL', 'PALADINO', 1, '+1dA DE RESISTÊNCIA E +4 DE ESPÍRITO', '', 'DF'),
('VIB', 'VIBRATA', 2, 'SUCESSO GARANTIDO EM 1DA DE DEFESA, +4
EM CORPO E +4 EM FOCO', 'CRUZADO Lv 7
BARDO Lv 7', 'DF'),
('KAL', 'KALINIER', 2, '+M DE VIDA, +4 EM MENTE E +4 EM ESPÍRITO', 'DRUIDA Lv 7
PALADINO Lv 7', 'DF'),
('CHE', 'CHEVALIER', 2, 'SUCESSO GARANTIDO EM 1DA DE
RESISTÊNCIA, +4 EM CORPO E +4 EM ESPÍRITO', 'CRUZADO Lv 7
PALADINO Lv 7', 'DF'),
('ENC', 'ENCANTADOR', 2, 'SUCESSO GARANTIDO EM 1DA DE ARTES, +4
EM MENTE E +4 EM FOCO', 'DRUIDA Lv 7
BARDO Lv 7', 'DF'),
('VAL', 'VALETE', 1, '+1dA DE ESQUIVA E +4 DE CORPO', '', 'CT'),
('AQU', 'ÁQUILA', 1, '+1dA DE ACERTO E +4 DE FOCO', '', 'CT'),
('TEC', 'TECNOCLASTA', 1, '+1dA DE ARTES E +4 DE MENTE', '', 'CT'),
('ILU', 'ILUSIONISTA', 1, '+1dA DE RESISTÊNCIA E +4 DE ESPÍRITO', '', 'CT'),
('LAN', 'LANCET', 2, 'SUCESSO GARANTIDO EM 1dA DE ESQUIVA, +4
EM CORPO E +4 EM FOCO', 'VALETE Lv 7
ÁQUILA Lv 7', 'CT'),
('TIM', 'TIMESEER', 2, 'SUCESSO GARANTIDO EM 1dA DE ARTES, +4
EM MENTE E +4 EM ESPÍRITO', 'TECNOCLASTA Lv 7
ILUSIONISTA Lv 7', 'CT'),
('PHA', 'PHASER', 2, 'SUCESSO GARANTIDO EM 1dA DE RESISTÊNCIA,
+4 EM CORPO E +4 EM ESPÍRITO', 'VALETE Lv 7
ILUSIONISTA Lv 7', 'CT'),
('GUN', 'GUNSLINGER', 2, 'SUCESSO GARANTIDO EM 1dA DE ACERTO, +4
EM MENTE E +4 EM FOCO', 'ÁQUILA Lv 7
TECNOCLASTA Lv 7', 'CT');

SET FOREIGN_KEY_CHECKS = 1;
