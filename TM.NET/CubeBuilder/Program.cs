using GBX.NET;
using GBX.NET.LZO;
using GBX.NET.Engines.GameData;
using GBX.NET.Engines.Meta;
using GBX.NET.Engines.Plug;
using Microsoft.Extensions.Logging;
using TmEssentials;

Gbx.LZO = new Lzo();

using ILoggerFactory factory = LoggerFactory.Create(builder => builder.AddSystemdConsole());
ILogger logger = factory.CreateLogger<Program>();

var gbx = Gbx.Parse<CGameItemModel>(Path.Combine("Assets", "PlasticCubeDyna.Item.Gbx"));
var node = gbx.Node;

logger.LogInformation("Name: {name}", node.Name);

if (node.EntityModel is CPlugPrefab prefab)
{
    foreach (var entRef in prefab.Ents)
    {
        if (entRef.Model is NPlugDyna_SKinematicConstraint kinematicConstraint)
        {
            logger.LogInformation("AngleMinDeg: {angle}", kinematicConstraint.AngleMinDeg);
            logger.LogInformation("AngleMaxDeg: {angle}", kinematicConstraint.AngleMaxDeg);
            foreach (var subFunc in kinematicConstraint.RotAnimFunc?.SubFuncs ?? [])
            {
                logger.LogInformation("RotAnimFunc:");
                logger.LogInformation("- Duration: {duration}", subFunc.Duration);
                logger.LogInformation("- Ease: {ease}", subFunc.Ease);
                logger.LogInformation("- Reverse: {reverse}", subFunc.Reverse);
            }

            logger.LogInformation("TransMin: {transMin}", kinematicConstraint.TransMin);
            logger.LogInformation("TransMax: {transMax}", kinematicConstraint.TransMax);
            foreach (var subFunc in kinematicConstraint.TransAnimFunc?.SubFuncs ?? [])
            {
                logger.LogInformation("TransAnimFunc:");
                logger.LogInformation("- Duration: {duration}", subFunc.Duration);
                logger.LogInformation("- Ease: {ease}", subFunc.Ease);
                logger.LogInformation("- Reverse: {reverse}", subFunc.Reverse);
            }

            kinematicConstraint.TransAnimFunc = new NPlugDyna_SKinematicConstraint.AnimFunc
            {
                IsDuration = true,
                SubFuncs = [
                    new NPlugDyna_SKinematicConstraint.SubAnimFunc
                    {
                        Duration = TimeInt32.FromSeconds(4),
                        Ease = NPlugDyna_SKinematicConstraint.AnimEase.Constant,
                        Reverse = false,
                    },
                    new NPlugDyna_SKinematicConstraint.SubAnimFunc
                    {
                        Duration = TimeInt32.FromSeconds(1),
                        Ease = NPlugDyna_SKinematicConstraint.AnimEase.QuadIn,
                        Reverse = false,
                    },
                    new NPlugDyna_SKinematicConstraint.SubAnimFunc
                    {
                        Duration = TimeInt32.FromSeconds(4),
                        Ease = NPlugDyna_SKinematicConstraint.AnimEase.Constant,
                        Reverse = true,
                    },
                    new NPlugDyna_SKinematicConstraint.SubAnimFunc
                    {
                        Duration = TimeInt32.FromSeconds(1),
                        Ease = NPlugDyna_SKinematicConstraint.AnimEase.QuadIn,
                        Reverse = true,
                    },
                ],
            };
        }
    }
}

node.Name = "PlasticCube-4-1-4-1";
node.Ident = new Ident("", "Stadium2020", "EwzZecOLSkW3kqn4sJYBuw");

Directory.CreateDirectory("GeneratedFiles");
gbx.Save(Path.Combine("GeneratedFiles", $"{node.Name}.Item.Gbx"));
