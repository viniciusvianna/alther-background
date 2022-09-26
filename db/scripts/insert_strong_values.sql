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

INSERT INTO PERSONAGENS (DETALHES) VALUES (
'{"nome_personagem":"Raeniel","escola":{"id_escola":"DV","nome_escola":"Desbravadores do Vazio"},"raca":{"id_raca":"RAE","nome_raca":"Rae","nome_habilidade_racial":"PASSO OBSCURO","descricao_habilidade_racial":"Os rae possuem uma habilidade única de caminhar brevementev pelo limiar das dimensões. Em batalha, o rae pode utilizar 5 pontos de mente para usar essa habilidade como ação padrão e ficar invisível para todos os outros que não sejam rae e que não tenham visão do limiar. Então, ele pode se mover livremente pelo campo. Sua próxima ação padrão cancela este estado. Fora de batalha ele pode fazer um teste de perícia mental para andar invisível. A distância determina a CD do teste.","nome_restricao_racial":"HEMATÓFAGOS","descricao_restricao_racial":"Rae se alimentam apenas de sangue animal, porém eles gostam muito de sangue. Caso um rae veja sangue vermelho em determinada quantidade ele deve fazer um teste de resistência. Caso fracasse, o rae estará inebriado e receberá -2NP nos dados de acerto de suas ações. A cada turno ele deve refazer o teste, enquanto estiver inebriado."},"aspiracao":{"id_aspiracao":"OF","nome_aspiracao":"Ofensor"},"origem":"Valiant","idade":50,"peso":80.5,"altura":182,"nivel":1,"XP":{"total":0,"atual":0},"PD":0,"PV":{"total":50,"atual":40,"temp":0},"AM":1,"AP":1,"moeda":"100 valores","inventario":"","anotacoes":"","atributos":{"corpo":{"total":10,"atual":10,"temp":0,"treino":0},"mente":{"total":15,"atual":15,"temp":0,"treino":1},"foco":{"total":10,"atual":10,"temp":0,"treino":0},"espirito":{"total":18,"atual":18,"temp":0,"treino":2},"social":{"total":8,"atual":8,"temp":0,"treino":0},"natureza":{"total":12,"atual":12,"temp":0,"treino":1}},"equipamentos":{"mao_direita":{"id_equipamento":"ADGBRZ","nome_equipamento":"Adaga de Bronze","efeito_equipamento":"","dados_equipamento":{"dano":"1d6+F4","acerto":"+1d6","artes":"","defesa":"","esquiva":"","resistencia":"","PV":""}},"mao_esquerda":{"id_equipamento":"","nome_equipamento":"","efeito_equipamento":"","dados_equipamento":{"dano":"","acerto":"","artes":"","defesa":"","esquiva":"","resistencia":"","PV":""}},"tronco":{"id_equipamento":"RBESMP","nome_equipamento":"Robe Simples","efeito_equipamento":"","dados_equipamento":{"dano":"","acerto":"","artes":"+1d8","defesa":"","esquiva":"+1d6","resistencia":"+1d4","PV":"+5"}}},"acessorios":{"maos":{"id_acessorio":"","nome_acessorio":"","efeito_acessorio":""},"tronco":{"id_acessorio":"","nome_acessorio":"","efeito_acessorio":""},"cabeca":{"id_acessorio":"ELMCER","nome_acessorio":"Elmo Cerimonial","efeito_acessorio":"Restaura 5 de PD quando sofre dano artístico"},"pes":{"id_acessorio":"","nome_acessorio":"","efeito_acessorio":""}},"acoes":{"acerto":{"d4":0,"d6":0,"d8":1,"d10":0,"d12":0,"d20":0},"esquiva":{"d4":0,"d6":0,"d8":1,"d10":0,"d12":0,"d20":0},"defesa":{"d4":0,"d6":0,"d8":1,"d10":0,"d12":0,"d20":0},"resistencia":{"d4":0,"d6":0,"d8":1,"d10":0,"d12":0,"d20":0},"artes":{"d4":0,"d6":0,"d8":1,"d10":0,"d12":0,"d20":0}},"caminhos_disponiveis":[{"id_caminho":"MON","nome_caminho":"Monge","tier":1,"nivel":0,"PC":{"total":0,"atual":0},"mestre":false},{"id_caminho":"NEB","nome_caminho":"Nébulo","tier":1,"nivel":0,"PC":{"total":0,"atual":0},"mestre":false},{"id_caminho":"ARC","nome_caminho":"Arcante","tier":1,"nivel":1,"PC":{"total":150,"atual":50},"mestre":false},{"id_caminho":"SHE","nome_caminho":"Shepian","tier":1,"nivel":0,"PC":{"total":0,"atual":0},"mestre":false}],"caminho_ativo":"ARC","habilidades_adquiridas":[{"id_habilidade":"MONITS","id_caminho":"MON","categoria":"intrinseca","nome_habilidade":"Combo","descricao_habilidade":""},{"id_habilidade":"NEBITS","id_caminho":"NEB","categoria":"intrinseca","nome_habilidade":"Névoa","descricao_habilidade":""},{"id_habilidade":"ARCITS","id_caminho":"ARC","categoria":"intrinseca","nome_habilidade":"Disparo","descricao_habilidade":""},{"id_habilidade":"SHEITS","id_caminho":"SHE","categoria":"intrinseca","nome_habilidade":"Avatar","descricao_habilidade":""},{"id_habilidade":"ENGARC","id_caminho":"ARC","categoria":"padrao","nome_habilidade":"Energia Arcana","descricao_habilidade":""}],"habilidades_equipadas":{"intrinseca":"ARCITS","padrao1":"ENGARC","padrao2":"","padrao3":"","padrao4":"","suporte1":"","suporte2":"","movimento":"","reacao":"","perfeita":""}}'
);

INSERT INTO HABILIDADES VALUES (
'MONITS',
'COMBO',
'INTRINSECA',
'Ao realizar um ataque físico com sucesso, o monge pode jogar seu acerto com -1dA para um segundo golpe no mesmo ataque. O dano é calculado ao fim do combo. Todos os efeitos de ataque (itens, habilidades ou crítico) só se aplicam ao primeiro golpe do combo.',
0,
'MON'
),(
'MONH11',
'PUMMEL I',
'PADRAO',
'Ao acertar os dois primeiros golpes do combo, o monge pode jogar seu acerto com -2dA para um terceiro golpe no mesmo ataque. O dano é calculado ao fim do combo.',
50,
'MON'
),(
'MONH12',
'PUMMEL II',
'PADRAO',
'Ao acertar os dois primeiros golpes do combo, o monge pode jogar seu acerto com -2dA para um terceiro golpe no mesmo ataque. Se acertar este golpe, ele pode jogar seu acerto com -3dA para um quarto golpe no mesmo ataque. O dano é calculado ao fim do combo.',
200,
'MON'
),(
'MONH13',
'PUMMEL III',
'PADRAO',
'Ao acertar os dois primeiros golpes do combo, o monge pode jogar seu acerto com -2dA para um terceiro golpe no mesmo ataque. Se acertar este golpe, ele pode jogar seu acerto com -3dA para um quarto golpe no mesmo ataque. Se acertar este golpe, ele pode jogar seu acerto com -4dA para um quinto golpe no mesmo ataque. O dano é calculado ao fim do combo.',
350,
'MON'
),(
'MONH20',
'NÊMESIS',
'MOVIMENTO',
'Os ataques do monge, ao acertarem com sucesso um inimigo, marcam o mesmo. O monge pode se mover livremente (independente de seu movimento padrão) para atacar um inimigo marcado. Só pode haver um inimigo marcado por vez. Caso o inimigo ataque outro combatente que não seja o monge, ele concede vantagem de combate para o monge.',
100,
'MON'
),(
'MONH30',
'ISOLAR',
'PADRAO',
'O monge libera uma onda de choque que afasta os inimigos ao redor exceto o último que ele atacou. Cause C4 de dano aos inimigos atingidos.',
50,
'MON'
),(
'MONH40',
'NIRVANA',
'PADRAO',
'O monge se concentra por um turno para depois causar C4 a mais de dano em todos os seus ataques e ganhar vantagem de combate contra o último inimigo que o feriu, por um turno. Ao atingir o nível máximo de caminho, esta habilidade fica ativa durante todo o resto do combate.',
250,
'MON'
),(
'MONH50',
'HAMEDO',
'REACAO',
'Ao ser atacado com sucesso, o monge pode atacar seu oponente primeiro, desde que esteja no seu alcance. Caso ele obtenha sucesso, ele realiza seu ataque primeiro. Ele não pode combar ao ativar esta habilidade.',
600,
'MON'
),(
'MONH61',
'MAHARASHI',
'SUPORTE',
'Ataques subsequentes do mesmo inimigo no monge causam C4 de dano a menos. Ataques subsequentes do monge no mesmo inimigo curam o monge em D4.',
100,
'MON'
),(
'MONH62',
'MAHARASHI II',
'SUPORTE',
'Ataques subsequentes do mesmo inimigo no monge causam C3 de dano a menos. Ataques subsequentes do monge no mesmo inimigo curam o monge em D3.',
200,
'MON'
),(
'MONH63',
'MAHARASHI III',
'SUPORTE',
'Ataques subsequentes do mesmo inimigo no monge causam C2 de dano a menos. Ataques subsequentes do monge no mesmo inimigo curam o monge em D2.',
300,
'MON'
),(
'MONPFT',
'COMBO PERFEITO',
'PERFEITA',
'Ataques subsequentes do monge no mesmo inimigo causam dano extra em uma série crescente: C4, C2, C e 2C. Ao fim da série os bônus resetam.',
500,
'MON'
);

INSERT INTO HABILIDADES VALUES (
'NEBITS',
'NÉVOA',
'INTRINSECA',
'Utilizando uma ação padrão, nébulos podem se tornar ocultos no campo de batalha. Inimigos podem procurar pelo nébulo realizando um teste de perícia de foco contra a esquiva do nébulo. Tomar uma ação de movimento não cancela o ocultamento.',
0,
'NEB'
),(
'NEBH11',
'ATAQUE SURPRESA I',
'PADRAO',
'Se estiver oculto de um inimigo, o ataque do nébulo causa F3 a mais de dano e ignora 1dZ de defesa do inimigo além da vantagem de combate.',
50,
'NEB'
),(
'NEBH12',
'ATAQUE SURPRESA II',
'PADRAO',
'Se estiver oculto de um inimigo, o ataque do nébulo causa F2 a mais de dano e ignora 1dZ de defesa do inimigo além da vantagem de combate.',
200,
'NEB'
),(
'NEBH13',
'ATAQUE SURPRESA III',
'PADRAO',
'Se estiver oculto de um inimigo, o ataque do nébulo causa F a mais de dano e ignora 1dZ de defesa do inimigo além da vantagem de combate.',
350,
'NEB'
),(
'NEBH20',
'ESFUMAÇAR',
'REACAO',
'Ao ser atacado com sucesso, o nébulo se desfaz em fumaça na frente do inimigo e está oculto até que tome outra ação padrão.',
100,
'NEB'
),(
'NEBH30',
'LEDO ENGANO',
'REACAO',
'Inimigos que tentam atacar o nébulo e erram concedem vantagem de combate ao nébulo em seu próximo turno e sofrem F2 a mais de dano.',
150,
'NEB'
),(
'NEBH40',
'OBSCURECIDO',
'MOVIMENTO',
'Ao se movimentar, o nébulo o faz tão rápido que confunde inimigos que estejam em combate direto com ele, tornando-se oculto para eles até seu próximo turno.',
300,
'NEB'
),(
'NEBH50',
'UMBRA',
'PADRAO',
'O nébulo usa a energia das artes para cegar os inimigos ao redor por 3 turnos. Todos os aliados estão ocultos durante esse período e tomar ações de movimento não desfaz o ocultamento. Gera 10 PD.',
300,
'NEB'
),(
'NEBH61',
'BACKSTAB I',
'SUPORTE',
'Ao realizar um ataque contra um inimigo em combate direto com um aliado, o nébulo causa +F3 de dano e ganha vantagem de combate contra o inimigo.',
100,
'NEB'
),(
'NEBH62',
'BACKSTAB II',
'SUPORTE',
'Ao realizar um ataque contra um inimigo em combate direto com um aliado, o nébulo causa +F2 de dano e ganha vantagem de combate contra o inimigo.',
200,
'NEB'
),(
'NEBH63',
'BACKSTAB III',
'SUPORTE',
'Ao realizar um ataque contra um inimigo em combate direto com um aliado, o nébulo causa +F de dano e ganha vantagem de combate contra o inimigo.',
300,
'NEB'
),(
'NEBPFT',
'FURTIVIDADE PERFEITA',
'PERFEITA',
'Até que realize uma ação padrão, o nébulo está oculto no combate. Ao realizar uma ação padrão, faça um teste de foco contra o acerto dos oponentes. Em caso de sucesso, o nébulo permanece oculto para todos os inimigos que não foram atacados por ele naquele turno.',
500,
'NEB'
);

INSERT INTO HABILIDADES VALUES (
'ARCITS',
'DISPARO',
'INTRINSECA',
'O arcante pode disparar um raio simples de energia da dimensão que acessa como uma ação padrão, causando 1d8 + M4 de dano em uma pequena área (AOE(1)) onde acerta. Gera 5 PD.',
0,
'ARC'
),(
'ARCH11',
'ENERGIA ARCANA I',
'SUPORTE',
'Você pode adquirir esta habilidade até 3 vezes. A cada vez que é adquirida aumente 1 dado de dano de mesmo nível de suas artes,diminua em 1 o fator de M e some 150 PC ao custo desta habilidade.',
50,
'ARC'
),(
'ARCH12',
'ENERGIA ARCANA II',
'SUPORTE',
'Aumente 2 dados de dano do mesmo nível de suas artes e diminua em 2 o fator de M.',
200,
'ARC'
),(
'ARCH13',
'ENERGIA ARCANA III',
'SUPORTE',
'Aumente 3 dados de dano do mesmo nível de suas artes e diminua em 3 o fator de M.',
350,
'ARC'
),(
'ARCH20',
'EQUILIBRIUM',
'SUPORTE',
'O arcante gera metade dos PD normais quando utiliza suas artes (arredondado para cima).',
300,
'ARC'
),(
'ARCH30',
'KETHEROS',
'PADRAO',
'O arcante canaliza grande quantidade de energia da dimensão que acessa em forma de uma bomba que explode em uma área média (AOE(2)), causando 1d10 + M4 de dano. Gera 10 PD.',
200,
'ARC'
),(
'ARCH40',
'SCATHE',
'PADRAO',
'O arcante faz um disparo de energia da dimensão que acessa atingindo uma grande área (AOE(3)) na sua frente e causando 1d12 + M4 de dano. Gera 20 PD',
500,
'ARC'
),(
'ARCH50',
'KARMA',
'REACAO',
'Ao sofrer dano, a próxima arte que o arcante utilizar não gera pontos de desequilíbrio. Este efeito não acumula para artes subsequentes.',
100,
'ARC'
),(
'ARCH61',
'MEDITAÇÃO I',
'SUPORTE',
'Cada turno que o arcante passa sem utilizar artes, restaura seus PD em 5.',
100,
'ARC'
),(
'ARCH62',
'MEDITAÇÃO II',
'SUPORTE',
'Cada turno que o arcante passa sem utilizar artes, restaura seus PD em 10.',
200,
'ARC'
),(
'ARCH63',
'MEDITAÇÃO III',
'SUPORTE',
'Cada turno que o arcante passa sem utilizar artes, restaura seus PD em 15.',
300,
'ARC'
),(
'ARCPFT',
'CONJURAÇÃO PERFEITA',
'PERFEITA',
'As artes do arcante não ferem aliados ou curam inimigos.',
500,
'ARC'
);

SET FOREIGN_KEY_CHECKS = 1;
