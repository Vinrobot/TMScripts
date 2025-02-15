using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using ItemCreator.Models;

namespace ItemCreator.ViewModels;

public partial class MainViewModel : ObservableRecipient
{
    public ObservableCollection<Animation> Animations { get; } = [];

    public MainViewModel()
    {
    }

    [RelayCommand]
    private void AddAnimation()
    {
        Animations.Add(new Animation());
    }

    [RelayCommand]
    private void RemoveAnimation(Animation animation)
    {
        Animations.Remove(animation);
    }
}
